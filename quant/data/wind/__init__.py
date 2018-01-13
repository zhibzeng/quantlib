"""Wind数据库接口"""
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

__all__ = ['WindDB', 'tables']


class WindDB:
    """Wind Financial Database"""
    def __init__(self):
        self.wind_connection = None
        self.__registry = self._init_registry()

    def _init_registry(self):
        try:
            with open(os.path.join(DATA_PATH, "registry.pkl"), "rb") as f:
                registry = pickle.load(f)
        except:
            registry = dict()
        return registry

    def _get_last_update(self, table_name, default=None):
        return self.__registry.get(table_name, default)

    def _set_last_update(self, table_name, time):
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
            要取权重的数据表
        s_info_windcode
            要取权重的指数的万得代码
        """
        # data = self.get_wind_table(table, columns=["trade_dt", "s_con_windcode", "i_weight", "s_info_windcode"])
        # data = data[data.s_info_windcode == s_info_windcode]
        table = self._get_table(table)
        columns = [table.trade_dt, table.i_weight, table.s_con_windcode]
        sql_statement = sql.select(columns).select_from(table).where(table.s_info_windcode==s_info_windcode)
        conn = self.get_wind_connection().engine
        data = pd.read_sql(sql_statement, conn, parse_dates={"trade_dt": "%Y%m%d"})
        data = data.pivot(index="trade_dt", columns="s_con_windcode", values="i_weight")
        return data.sort_index()

    @LOCALIZER.wrap("wind_basics.h5", const_key="basics", format="fixed")
    def get_stock_basics(self) -> pd.DataFrame:
        table = self.get_wind_table("AShareDescription")
        table.set_axis(table.s_info_windcode, axis=0)
        return table.drop("s_info_windcode", axis=1)

    # @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "field"], format="fixed")
    def arrange_entry_table(self, table: str, field: str="", columns: str=None, default_value=None):
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
            default_value
                当一个日期不在任何entry_dt和remove_dt之间时，默认的值。如果为空，则使用对应字段类型的默认值。
        """
        from ...utils.calendar import TDay
        if isinstance(table, str):
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
            assert set(columns).issubset(column_names):
        else:
            raise TypeError("table must be either a str or DataFrame")

        start_date = min(pd.to_datetime("2006-01-01"), table.entry_dt.min())
        end_date = max(pd.to_datetime(date.today()), table.remove_dt.max())
        index = pd.date_range(start_date, end_date, freq=TDay)
        
        basics = self.get_stock_basics().dropna(subset=['s_info_listdate'])
        basics = basics[pd.isnull(basics.s_info_delistdate)]
        columns = basics.index

        if not field:
            data = pd.DataFrame(np.full((len(index), len(columns)), False, dtype=bool), index=index, columns=columns)
        else:
            data = pd.DataFrame(np.full((len(index), len(columns)), default_value or table[field].dtype.type(), dtype=table[field].dtype), index=index, columns=columns)
        
        for _, row in table.iterrows():
            key = row[column]
            if key not in columns:
                continue
            start = row.entry_dt
            end = row.remove_dt
            if pd.isnull(end):
                end = end_date
            if not field:
                data.loc[start:end, key] = True
            else:
                data.loc[start:end, key] = row[field]
        data.index.freq = None      # Can't save to hdf with freq
        return data

    # @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "level"])
    def get_stock_industries(self, table: str, level: int) -> pd.DataFrame:
        """
        从指定的表中获取股票行业表

        Parameters
        ==========
        table: str
            AShareIndustriesClass 中国A股行业分类
            AShareSECNIndustriesClass 中国A股证监会新版行业分类
            AShareSECIndustriesClass 中国A股证监会行业分类
            AShareIndustriesClassCITICS 中国A股中信行业分类
        level: {1, 2, 3} 行业等级
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
        industry = wind.get_wind_table(table, ["s_info_windcode", field_name, "entry_dt", "remove_dt"])
        industry[field_name] = industry[field_name].str[:lengths[level]]
        industry = self.arrange_entry_table(industry, field_name).bfill().replace(industry_codes, industry_names)
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
