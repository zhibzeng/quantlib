"""Wind数据库接口"""
import os
import sys
import pickle
from inspect import signature
from datetime import date, datetime
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.sql import select, and_
from dateutil.parser import parse
from . import tables
from ...common.localize import LOCALIZER
from ...common.settings import CONFIG, DATA_PATH
from ...common.db.sql import SQLClient

__all__ = ['WindDB', 'tables']


class WindDB:
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

    def _get_last_update(self, table_name):
        return self.__registry.get(table_name)

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
            )
        return self.wind_connection

    def _get_table(self, table_name):
        engine = self.get_wind_connection().engine
        meta = sa.MetaData()
        table = sa.Table(table_name, meta, autoload=True, autoload_with=engine)
        return table

    def _check_columns(self, table_name, columns):
        if not columns:
            table = self._get_table(table_name)
            columns = set(col.name for col in table.columns)
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
        last_update = self._get_last_update(table_name)
        table = self._get_table(table_name)
        columns = set(columns)
        columns.add("object_id")
        parse_dates = {col: "%Y%m%d" for col in columns if col.endswith("_dt") or col.endswith("date")}
        opdate = list(filter(lambda col: col.name.lower() == "opdate", table.columns))[0]
        sql_statement = select([sa.Column(col) for col in columns]).select_from(table)
        if last_update:
            sql_statement = sql_statement.where(opdate <= last_update)
        engine = self.get_wind_connection().engine
        df = pd.read_sql_query(sql_statement, engine, index_col="object_id", parse_dates=parse_dates)
        filename = os.path.join(DATA_PATH, "wind.h5")
        for col in df.columns:
            df[col].to_hdf(filename, key="/".join([table_name, col]), format="table", append=True, complevel=9)

    def _update_wind_table(self, table_name):
        last_update = self._get_last_update(table_name) or parse("2000-01-01")
        table = self._get_table(table_name)
        columns = self._get_dataset_columns(table_name)
        parse_dates = {col: "%Y%m%d" for col in columns if col.endswith("_dt") or col.endswith("date")}
        opdate = list(filter(lambda col: col.name.lower() == "opdate", table.columns))[0]
        sql_statement = select(columns).select_from(table)
        sql_statement = sql_statement.where(opdate > last_update)
        engine = self.get_wind_connection().engine
        df = pd.read_sql_query(sql_statement, engine, index_col="object_id", parse_dates=parse_dates)
        filename = os.path.join(DATA_PATH, "wind.h5")
        for col in df.columns:
            df[col].to_hdf(filename, key="/".join([table_name, col]), format="table", append=True, complevel=9)
        self._set_last_update(table_name, datetime.now())

    def get_wind_table(self, table_name, columns=None):
        non_existing_columns = self._check_columns(table_name, columns)
        if non_existing_columns:
            self._add_wind_columns(table_name, non_existing_columns)
        columns = columns or self._get_dataset_columns(table_name)
        filename = os.path.join(DATA_PATH, "wind.h5")
        data = {}
        for col in columns:
            data[col] = pd.read_hdf(filename, key="/".join([table_name, col]))
        return pd.DataFrame(data)

    # def _update_wind_table(self, table_name, columns=None):
    #     """
    #     update the local cache of Wind Database table

    #     Parameters
    #     ----------
    #     table_name: str
    #         the table name to be updated
    #     """
    #     filename = os.path.join(DATA_PATH, "wind.h5")
    #     table = getattr(tables, table_name)
    #     columns = table.__table__.columns
    #     wind_connection = self.get_wind_connection()
    #     sql_statement = select(columns)
    #     parse_dates = {col.name: "%Y%m%d" for col in columns if col.name.endswith("_dt") or col.name.endswith("date")}
    #     # last_update = self._get_last_update(table_name) or "2000-01-01"
    #     # sql_statement = sql_statement.where(table.opdate > last_update)
    #     # data = pd.read_sql(sql_statement, wind_connection.engine, parse_dates=parse_dates)

    #     last_update = self._get_last_update(table_name)
    #     if last_update:
    #         sql_statement = sql_statement.where(table.opdate > last_update)
    #     data = pd.read_sql_query(sql_statement, wind_connection.engine, parse_dates=parse_dates, index_col="object_id")

    #     data.to_hdf(filename, table_name, format="table", append=True, complevel=9, dropna=True)
        
    #     # self.set_last_update(table_name, data.opdate.max())
    #     self._set_last_update(table_name, datetime.now())
    #     # data = pd.read_hdf(filename, table_name)
    #     if columns:
    #         return data[[col.name for col in columns if col.name.lower() != "object_id"]]
    #     else:
    #         return data

    # def get_wind_table(self, table_name, columns=None):
    #     filename = os.path.join(DATA_PATH, "wind.h5")
    #     try:
    #         data = pd.read_hdf(filename, table_name, columns=columns)
    #     except (FileNotFoundError, KeyError):
    #         data = self._update_wind_table(table_name, columns=columns)
    #     # assert data.index.is_monotonic_increasing, "not monotonic increasing"
    #     assert not data.index.duplicated().any(), "index duplicated"
    #     return data

    @LOCALIZER.wrap("wind_pivot.h5", keys=["table", "field"])
    def get_wind_data(self, table, field, index=None, columns=None):
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
        data = self.get_wind_table(table, columns=[field, index, columns])
        return data.pivot(index=index, columns=columns, values=field)

    @LOCALIZER.wrap("wind_index_weight.h5", keys=["table", "s_info_windcode"])
    def get_index_weight(self, table, s_info_windcode):
        """从指定的表中获得指数权重

        Parameters
        ----------
        table
            要取权重的数据表
        s_info_windcode
            要取权重的指数的万得代码
        """
        data = self.get_wind_table(table, columns=["trade_dt", "s_con_windcode", "i_weight", "s_info_windcode"])
        data = data[data.s_info_windcode == s_info_windcode]
        data = data.pivot(index="trade_dt", columns="s_con_windcode", values="i_weight")
        return data

