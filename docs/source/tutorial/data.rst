Wind Data
*********

直接从万得SQL数据库查询数据，需要设置数据库连接信息。


Configure
#########

配置文件``~/.quantlib/config.cfg``:

wind_db_driver = 'pymysql'
wind_db_type = 'mysql'
wind_host = 'localhost'
wind_port = 3306
wind_username = 'wind'
wind_password = 'password'
wind_db_name = 'quant'

量价数据
#######

..  code-block::
    python

    import quant.data.wind as wind
    wind.get_wind_data("AShareEODPrices", "s_dq_pctchange")