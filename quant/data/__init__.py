from .wind import WindDB, to_trade_data


try:
    wind = WindDB()
except:
    wind = None
