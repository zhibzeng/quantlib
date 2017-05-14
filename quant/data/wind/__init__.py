"""Wind数据库接口"""
from ...common.localize import LOCALIZER
from . import tables
from ...common.settings import CONFIG
from ...common.db.sql import SQLClient


WIND_CONNECTION = SQLClient(
    host=CONFIG.WIND_HOST,
    port=CONFIG.WIND_PORT,
    db_driver=CONFIG.WIND_DB_DRIVER,
    db_type=CONFIG.WIND_DB_TYPE,
    username=CONFIG.WIND_USERNAME,
    password=CONFIG.WIND_PASSWORD,
)


def __get_field(table, fieldname):
    if hasattr(table, fieldname):
        return getattr(table, fieldname)
    raise AttributeError("Table `%s` has no field `%s`" % (table.__tablename__, fieldname))
    


def __get_fields(table, fieldnames):
    if isinstance(fieldnames, list):
        return [__get_field(table, fieldname) for fieldname in fieldnames]
    else:
        return __get_field(table, fieldnames)


def get_wind_data(table, fields=None, **kwargs):
    """从Wind数据库获取数据
    """
    if fields:
        fields = __get_fields(table, fields)
    else:
        fields = table
    query = WIND_CONNECTION.session.query(fields)
    for key, value in kwargs.items():
        field = __get_field(table, key)
        if isinstance(value, list):
            query = query.filter(field.in_(value))
        else:
            query = query.filter(field == value)
    data = query.all()

