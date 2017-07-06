from .wind import WindDB


try:
    wind = WindDB()
except:
    wind = None
