"""SQL数据库连接"""

import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.types import VARCHAR, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class SQLClient:
    """简单的结构，包含一些SQL连接的信息"""
    def __init__(self,
                 host='localhost',
                 port=3306,
                 username='',
                 password='',
                 db_name='quant',
                 db_type='mysql',
                 db_driver='pymysql'):
        """
        获得数据库连接
        Args:
            host (str): 数据库地址
            port (str): 数据库端口
            username (str): 用户名
            password (str): 密码
            db_name (str): 数据库名
            db_type (str): 数据库类型，如mysql, mssql
            db_driver (str): 数据库驱动，如pymysql
        """
        self.sqlalchemy_conn_string = \
            '%(db_type)s+%(db_driver)s://%(username)s:%(password)s@%(host)s:%(port)s/%(db_name)s' %\
            dict(
                host=host,
                port=port,
                username=username,
                password=password,
                db_name=db_name,
                db_driver=db_driver,
                db_type=db_type,
            )
        self.engine = sqlalchemy.create_engine(self.sqlalchemy_conn_string, echo=False)
        self.session = sqlalchemy.orm.sessionmaker(bind=self.engine)()

    def table_names(self):
        """返回当前数据库下的所有表名"""
        return self.engine.table_names()

    def has_table(self, table_name, schema=None):
        """查询当前数据库下是否有指定的表名"""
        return self.engine.has_table(table_name, schema)

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            if hasattr(self.session, name):
                return getattr(self.session, name)
            else:
                raise AttributeError

