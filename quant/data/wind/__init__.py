"""Wind数据库接口"""
import sys
import pandas as pd
from sqlalchemy.sql import select
from . import tables
from ...common.localize import LOCALIZER
from ...common.settings import CONFIG
from ...common.db.sql import SQLClient

__all__ = ['get_sql_connection', 'tables', 'get_wind_data', 'get_wind_rawdata']

# TODO: A better data interface

__wind_connection = None
def get_sql_connection():
    """Returns a SQLClient object with settings in `config.cfg`"""
    global __wind_connection
    if __wind_connection is None:
        __wind_connection = SQLClient(
            host=CONFIG.WIND_HOST,
            port=CONFIG.WIND_PORT,
            db_driver=CONFIG.WIND_DB_DRIVER,
            db_type=CONFIG.WIND_DB_TYPE,
            db_name=CONFIG.WIND_DB_NAME,
            username=CONFIG.WIND_USERNAME,
            password=CONFIG.WIND_PASSWORD,
        )
    return __wind_connection


def __get_field(table, fieldname):
    if hasattr(table, fieldname):
        return getattr(table, fieldname)
    raise AttributeError("Table `%s` has no field `%s`" % (table.__tablename__, fieldname))


@LOCALIZER.wrap("wind")
def get_wind_rawdata(table, parse_dates=None) -> pd.DataFrame:
    """从Wind数据库获取数据

    Parameters
    ----------
    table: str
        要读的SQL表, 参考`quant.data.wind.tables`
    parse_dates
        参考`pd.read_sql`
    """
    if isinstance(table, str):
        table = getattr(tables, table)
    columns = table.__table__.columns
    wind_connection = get_sql_connection()
    parse_dates = parse_dates or {col: "%Y%m%d" for col in columns if col.endswith("_dt")}
    data = pd.read_sql(select(columns), wind_connection.engine, parse_dates=parse_dates)
    return data


@LOCALIZER.wrap("wind", exclude=['index', 'columns', 'parse_dates'])
def get_wind_data(table, field, index=None, columns=None, parse_dates=True):
    """从Wind数据库获取数据，并转换为以股票代码为列、日期为行的格式

    Parameters
    ----------
    table
        要读的SQL表, 参考`quant.data.wind.tables`
    field
        作为值的字段
    index
        作为index的字段
    columns
        作为columns的字段
    parse_dates: bool, optional
        是否将index字段转换为datetime

    Returns
    -------
        pd.DataFrame
    """
    if isinstance(table, str):
        table = getattr(tables, table)
    columns = columns or tables.DEFAULT_FIELDS[table]["columns"]
    index = index or tables.DEFAULT_FIELDS[table]["index"]
    field_ = __get_field(table, field)
    index_ = __get_field(table, index)
    columns_ = __get_field(table, columns)
    sql_statement = select([field_, index_, columns_])
    wind_connection = get_sql_connection()
    data = pd.read_sql(sql_statement, wind_connection.engine, parse_dates=parse_dates)
    data = data.pivot(index=index, columns=columns, values=field)
    return data


@LOCALIZER.wrap("index_weight")
def get_index_weight(table, s_info_windcode):
    """从指定的表中获得指数权重

    Parameters
    ----------
    table
        要取权重的数据表
    s_info_windcode
        要取权重的指数的万得代码
    """
    if isinstance(table, str):
        table = getattr(tables, table)
    wind_connection = get_sql_connection()
    columns = [table.i_weight, table.s_con_windcode, table.trade_dt]
    sql_statement = select(columns).where(table.s_info_windcode == s_info_windcode)
    data = pd.read_sql(sql_statement, wind_connection.engine, parse_dates={"trade_dt": "%Y%m%d"})
    data = data.pivot(index="trade_dt", columns="s_con_windcode", values="i_weight")
    return data
