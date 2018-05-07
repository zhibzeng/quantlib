"""Wind数据库接口"""
from collections import defaultdict
import os
import sys
import pickle
from inspect import signature
import warnings
from datetime import date, datetime
from typing import List, Union

import numpy as np
import pandas as pd
import sqlalchemy as sa
import sqlalchemy.sql as sql
from dateutil.parser import parse

from . import tables
from ...common.localize import LOCALIZER
from ...common.settings import CONFIG, DATA_PATH
from ...common.db.sql import SQLClient
from ...common.logging import Logger
from ...utils.calendar import TDay

__all__ = ['WindDB', 'tables', 'to_trade_data']


def to_trade_data(data):
    """
    把按季度公布的数据转换成交易日数据
    """
    today = date.today().strftime("%Y-%m-%d")
    target_index = pd.Series(pd.date_range(data.index[0], today, freq=TDay))
    index = sorted(set(target_index) | set(data.index))
    columns = data.columns
    final_data = pd.DataFrame(np.full((len(index), len(columns)), np.nan), index=index, columns=columns)
    final_data.update(data)
    final_data = final_data.ffill().loc[target_index]
    return final_data


class WindDB:
    """万得金融数据库借口"""
    def __init__(self):
        self.wind_connection = None
        self.__registry = self._init_registry()

    def _init_registry(self):
        """
        初始化注册表。注册表用于记录每个数据库的最后更新时间，方便增量更新
        """
        try:
            with open(os.path.join(DATA_PATH, "registry.pkl"), "rb") as f:
                registry = pickle.load(f)
        except:
            registry = dict()
        return registry

    def _get_last_update(self, table_name: str, default=None):
        """
        获取一个库的最后更新时间

        Parameters
        ==========
        table_name: str
            查询的数据库名称
        """
        return self.__registry.get(table_name, default)

    def _set_last_update(self, table_name, time):
        """
        更新一个库的最后更新时间

        Parameters
        ==========
        table_name: str
            查询的数据库名称
        """
        self.__registry[table_name] = time
        with open(os.path.join(DATA_PATH, "registry.pkl"), "wb") as f:
            pickle.dump(self.__registry, f)

    def get_wind_connection(self):
        if not self.wind_connection:
            self.wind_connection = SQLClient(
                host=CONFIG.WIND_HOST,
                port=CONFIG.WIND_PORT,
                db_driver=CONFIG.WIND_DB_DRIVER,
                db_type=CONFIG.WIND_DB_TYPE,
                db_name=CONFIG.WIND_DB_NAME,
                username=CONFIG.WIND_USERNAME,
                password=CONFIG.WIND_PASSWORD,
                charset=CONFIG.WIND_CHARSET
            )
        return self.wind_connection

    def _get_table(self, table_name):
        try:
            table = getattr(tables, table_name)
        except:
            engine = self.get_wind_connection().engine
            meta = sa.MetaData()
            table = sa.Table(table_name, meta, autoload=True, autoload_with=engine)
        return table

    def _check_columns(self, table_name, columns):
        if not columns:
            table = self._get_table(table_name)
            if isinstance(table, sql.schema.Table):
                columns = set(col.name for col in table.columns if col.name.lower() != "object_id")
            else:
                columns = set(col.name for col in table.__table__.columns if col.name.lower() != "object_id")
        elif isinstance(columns, str):
            columns = [columns]
        columns = set(map(str.lower, columns))
        existing_columns = self._get_dataset_columns(table_name)
        if not existing_columns:
            return columns
        else:
            return columns - set(existing_columns)

    def _get_dataset_columns(self, table_name):
        filename = os.path.join(DATA_PATH, "wind.h5")
        with pd.HDFStore(filename) as h5:
            data = [tuple(key[1:].split("/")) for key in h5.keys()]
        columns = [col for table, col in data if table.lower() == table_name.lower()]
        return columns

    def _add_wind_columns(self, table_name, columns):
        Logger.debug("Updating table [{table}] with columns {columns}".format(table=table_name, columns=columns))
        last_update = self._get_last_update(table_name)
        table = self._get_table(table_name)
        columns = set(columns)
        columns.add("object_id")
        parse_dates = {col: "%Y%m%d" for col in columns if col.endswith("_dt") or col.endswith("date")}
        if isinstance(table, sql.schema.Table):
            opdate = list(filter(lambda col: col.name.lower() == "opdate", table.columns))[0]
            opdate.table = table
            sql_statement = sql.select([sa.Column(col) for col in columns]).select_from(table)
        else:
            opdate = table.opdate
            sql_statement = sql.select([getattr(table, col.lower()) for col in columns])
        
        if last_update:
            sql_statement = sql_statement.where(opdate <= last_update)
        else:
            session = self.get_wind_connection().session
            last_update = session.query(sql.func.max(opdate))[0][0]
            self._set_last_update(table_name, last_update)
        Logger.debug(str(sql_statement))
        engine = self.get_wind_connection().engine
        df = pd.read_sql_query(sql_statement, engine, index_col="object_id", parse_dates=parse_dates)
        filename = os.path.join(DATA_PATH, "wind.h5")
        for col in df.columns:
            df[col].to_hdf(filename, key="/".join([table_name, col]), format="table", append=True, complevel=9)

    def _update_wind_table(self, table_name):
        sys.stdout.write("Updating table [{table}]..........".format(table=table_name))
        sys.stdout.flush()
        last_update = self._get_last_update(table_name, parse("2000-01-01"))
        table = self._get_table(table_name)
        columns = self._get_dataset_columns(table_name) + ["object_id"]
        parse_dates = {col: "%Y%m%d" for col in columns if col.endswith("_dt") or col.endswith("date")}
        opdate = sa.Column("opdate")
        sql_statement = sql.select([sa.Column(col) for col in columns]).select_from(table)
        sql_statement = sql_statement.where(opdate > last_update)
        engine = self.get_wind_connection().engine
        df = pd.read_sql_query(sql_statement, engine, index_col="object_id", parse_dates=parse_dates)
        if len(df) != 0:
            filename = os.path.join(DATA_PATH, "wind.h5")
            for col in df.columns:
                df[col].to_hdf(filename, key="/".join([table_name, col]), format="table", append=True, complevel=9)
        self._set_last_update(table_name, datetime.now())
        sys.stdout.write("\rUpdate table [{table}]..........[Done]\n\r{nrows} rows updated.\n".format(table=table_name, nrows=len(df)))
        sys.stdout.flush()

    def get_wind_table(self, table_name: str, columns: Union[List[str], str]=None, format="table") -> pd.DataFrame:
        """
        万得数据库原始表

        Parameters
        ==========
        table_name: str
            数据库中数据表的名称
        columns: List[str], 可选
            要查询的数据字段，如果为None则查询所有字段

        Returns
        =======
        pd.DataFrame

        Examples
        ========

        ..  code-block::
            python

            wind.get_wind_table("AShareEODPrices", ["s_info_windcode", "trade_dt", "s_dq_adjclose", "s_dq_adjopen"])
        """
        non_existing_columns = self._check_columns(table_name, columns)
        if non_existing_columns:
            self._add_wind_columns(table_name, non_existing_columns)
        columns = columns or self._get_dataset_columns(table_name)
        filename = os.path.join(DATA_PATH, "wind.h5")
        data = {}
        for col in columns:
            data[col] = pd.read_hdf(filename, key="/".join([table_name, col]))
            data[col] = data[col][~data[col].index.duplicated(keep="last")]
        return pd.DataFrame(data)

    @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "field"], format="fixed")
    def get_wind_data(self, table: str, field: str, index: str=None, columns: str=None) -> pd.DataFrame:
        """
        获取万得交易数据

        Parameters
        ==========
        table: str
            数据库中数据表的名称
        field: str
            要查询的字段名
        index: str
            要作为行的字段名，默认为trade_dt
        column: str
            要作为列的字段名，默认为s_info_windcode

        Examples
        ========

        ..  code-block::
            python

            wind.get_wind_data("AShareEODPrices", "s_dq_pctchange")
        """
        column_names = [col.name for col in getattr(tables, table).__table__.columns]
        if columns is None:
            if "s_info_windcode" in column_names:
                columns = "s_info_windcode"
            else:
                raise RuntimeError("No columns specified for DataFrame.pivot")
        if index is None:
            if "trade_dt" in column_names:
                index = "trade_dt"
            else:
                raise RuntimeError("No index specified for DataFrame.pivot")
        data = self.get_wind_table(table, columns=[field, index, columns]).drop_duplicates(subset=[index, columns], keep='last')
        return data.pivot(index=index, columns=columns, values=field).sort_index()

    @LOCALIZER.wrap("wind_index_weight.h5", keys=["table", "s_info_windcode"], format="fixed")
    def get_index_weight(self, table: str, s_info_windcode: str) -> pd.DataFrame:
        """从指定的表中获得指数权重

        Parameters
        ----------
        table
            要取权重的数据表，例如AIndexHS300FreeWeight
        s_info_windcode
            要取权重的指数的万得代码，中证500为000905.SH，沪深300为399300.SZ。

        Examples
        --------

        ..  code-block::
            python

            # 获取中证500指数的免费权重
            wind.get_index_weight("AIndexHS300FreeWeight", "000905.SH")
        """
        # data = self.get_wind_table(table, columns=["trade_dt", "s_con_windcode", "i_weight", "s_info_windcode"])
        # data = data[data.s_info_windcode == s_info_windcode]
        table = self._get_table(table)
        columns = [table.trade_dt, table.i_weight, table.s_con_windcode]
        sql_statement = sql.select(columns).select_from(table).where(table.s_info_windcode==s_info_windcode)
        conn = self.get_wind_connection().engine
        data = pd.read_sql(sql_statement, conn, parse_dates={"trade_dt": "%Y%m%d"})
        data = data.pivot(index="trade_dt", columns="s_con_windcode", values="i_weight").sort_index().fillna(0) / 100
        
        data = to_trade_data(data)
        return data

    @LOCALIZER.wrap("wind_basics.h5", const_key="basics", format="fixed")
    def get_stock_basics(self) -> pd.DataFrame:
        """
        从AShareDescription表中获取每个股票的基本信息
        """
        table = self.get_wind_table("AShareDescription")
        table.set_axis(table.s_info_windcode, axis=0)
        return table.drop("s_info_windcode", axis=1)

    @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "field", "columns"], format="fixed")
    def arrange_entry_table(self, table: str, field: str="", columns: str=None):
        """
        把带有entry_dt, remove_dt的表重新整理成以股票为列、日期为行的透视表

        Parameters
        ==========
            table: str
                要查询的表名，或DataFrame数据框
            field: str
                以某字段为内容。如果为空，则生成的数据只含有True，False
            columns: str
                指定要作为列名的字段，默认为s_info_windcode

        Examples
        ========

        ..  code-block::
            python

            # AShareST表示通过entry_dt和remove_dt来维护股票进入ST和离开ST的时间的
            # arrange_entry_table把该信息重新整理成以交易日为行、股票为列的“交易日”表
            # 最后把剩下的NA用False填充
            wind.arrange_entry_table("AShareST").fillna(False)
        """
        if isinstance(table, str):
            # 如果table是str，向数据库查询
            column_names = [col.name for col in getattr(tables, table).__table__.columns]
            if columns is None:
                if "s_info_windcode" in column_names:
                    column = "s_info_windcode"
                else:
                    raise RuntimeError("No columns specified for DataFrame.pivot")
            else:
                column = columns
            if "entry_dt" not in column_names or "remove_dt" not in column_names:
                raise RuntimeError("`entry_dt` and/or `remove_dt` not in columns. Maybe this table is not suitable for this operation")
            if field:
                columns = [field, "entry_dt", "remove_dt", column]
            else:
                columns = ["entry_dt", "remove_dt", column]
            table = self.get_wind_table(table, columns=columns)
        elif isinstance(table, pd.DataFrame):
            # 如果table是DataFrame，直接使用
            column_names = set(table.columns)
            if columns is None:
                if "s_info_windcode" in column_names:
                    column = "s_info_windcode"
                else:
                    raise RuntimeError("No columns specified for DataFrame.pivot")
            if "entry_dt" not in column_names or "remove_dt" not in column_names:
                raise RuntimeError("`entry_dt` and/or `remove_dt` not in columns. Maybe this table is not suitable for this operation")
            if field:
                columns = [field, "entry_dt", "remove_dt", column]
            else:
                columns = ["entry_dt", "remove_dt", column]
            assert set(columns).issubset(column_names)
        else:
            raise TypeError("table must be either a str or DataFrame")

        dtype = table[field].dtype if field else bool

        start_date = min(pd.to_datetime("2006-01-01"), table.entry_dt.min())
        end_date = max(pd.to_datetime(date.today()), table.remove_dt.max())
        index = pd.date_range(start_date, end_date, freq=TDay)
        
        basics = self.get_stock_basics().dropna(subset=['s_info_listdate'])
        basics = basics[pd.isnull(basics.s_info_delistdate)]
        columns = basics.index

        data = defaultdict(list)
        for _, row in table.iterrows():
            key = row[column]
            start = row.entry_dt
            end = end_date if pd.isnull(row.remove_dt) else row.remove_dt
            idx = pd.date_range(start, end, freq=TDay)
            value = [True if not field else row[field]] * len(idx)
            series = pd.Series(value, index=idx)
            data[key].append(series)
        data2 = []
        for key, item in data.items():
            series = pd.concat(item, 0).rename(key)
            series = series[~series.index.duplicated(keep='last')]
            data2.append(series)
        data = pd.concat(data2, 1)
        
        rest_columns = set(columns) - set(data.columns)
        if rest_columns:
            idx = pd.date_range(start_date, end_date, freq=TDay)
            data = pd.concat([data, pd.DataFrame(np.full((len(idx), len(rest_columns)), None, dtype=dtype), index=idx, columns=rest_columns)], 1) 
        return data

    def get_consensus_data(self, field: str, est_years: int=1) -> pd.DataFrame:
        """
        A股盈利预测汇总

        Parameters
        ==========

        field: str
            分析师预测数据字段
        est_years: {1, 2, 3}
            预测周期（年）

        Examples
        ========

        ..  code-block::
            python

            # 获取预测一年的平均每股收益
            wind.get_consensus_data('eps_avg', 1)
        """
        sql = """
        select s_info_windcode, est_dt, {}
        from AShareConsensusData
        where s_est_yeartype='FY{}'
        and consen_data_cycle_typ='263003000'
        order by opdate desc
        """.format(field, est_years)
        conn = self.get_wind_connection().engine
        df = pd.read_sql_query(sql, conn, parse_dates={'est_dt': '%Y%m%d'}).drop_duplicates(['s_info_windcode', 'est_dt'])
        pivot_table = df.pivot(index='est_dt', columns='s_info_windcode', values=field).ffill()
        return pivot_table

    @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "level"])
    def get_stock_industries(self, table: str, level: int=1) -> pd.DataFrame:
        """
        从指定的表中获取股票行业表

        Parameters
        ==========
        table: str

            AShareIndustriesClass 中国A股行业分类

            AShareSECNIndustriesClass 中国A股证监会新版行业分类

            AShareSECIndustriesClass 中国A股证监会行业分类

            AShareIndustriesClassCITICS 中国A股中信行业分类
        level: {1, 2, 3}
            行业等级

        Examples
        ========

        ..  code-block::
            python

            # 获取中国A股中信行业分类 （一级分类）
            wind.get_stock_industries("AShareIndustriesClassCITICS", 1)
        """
        level = level
        tables = {
            "AShareIndustriesClass": "wind_ind_code",
            "AShareSECNIndustriesClass": "sec_ind_code",
            "AShareSECIndustriesClass": "sec_ind_code",
            "AShareIndustriesClassCITICS": "citics_ind_code",
        }
        lengths = {
            1: 4,
            2: 6,
            3: 8
        }
        industry_codes = (self
            .get_wind_table("AShareIndustriesCode", ["industriesname", "industriescode", "levelnum"])
            .query("levelnum==@level+1")
        )
        industry_codes.industriescode = industry_codes.industriescode.str[:lengths[level]]
        industry_codes, industry_names = zip(*industry_codes[["industriescode", "industriesname"]].to_records(index=False))
        field_name = tables[table]
        industry = self.get_wind_table(table, ["s_info_windcode", field_name, "entry_dt", "remove_dt"])
        industry[field_name] = industry[field_name].str[:lengths[level]]
        catetory_dtype = pd.api.types.CategoricalDtype(categories=set(industry_names))
        industry = (self
            .arrange_entry_table(industry, field_name)
            .bfill()
            .replace(industry_codes, industry_names)
            .dropna(1, how='all')
        )
        return industry

    @LOCALIZER.wrap("wind_basics.h5", const_key="st")
    def get_stock_st(self) -> pd.DataFrame:
        from ...utils.calendar import TDay
        warnings.warn(DeprecationWarning(
            "This method is depreciated in favor of `arrange_entry_table`. "
            "Use wind.arrange_entry_table('AShareST').fillna(False)"))
        table = self.get_wind_table("AShareST")
        table = table[pd.isnull(table.remove_dt) | (table.remove_dt > "2006-01-01")]
        today = pd.to_datetime(date.today())

        basics = self.get_stock_basics().dropna(subset=['s_info_listdate'])
        basics = basics[pd.isnull(basics.s_info_delistdate) | (basics.s_info_delistdate > '2006-01-01')]
        columns = basics.index

        start_date = "2006-01-01"
        end_date = max(today, table.remove_dt.max())
        index = pd.date_range(start_date, end_date, freq=TDay)
        st_table = pd.DataFrame(np.full((len(index), len(columns)), False), index=index, columns=columns)
        for _, row in table.iterrows():
            key = row.s_info_windcode
            start = row.entry_dt
            if start < pd.to_datetime("2006-01-01"):
                start = "2006-01-01"
            end = row.remove_dt
            if pd.isnull(end):
                end = end_date
            daterange = pd.date_range(start, end, freq=TDay)
            st_table.loc[daterange, key] = True
        st_table.index.freq = None      # Can't save to hdf with freq
        return st_table
