import json
import ujson
import pytz
import numpy as np
import pandas as pd


class SerializerBase:
    @staticmethod
    def serialize(data):
        raise NotImplementedError

    @ staticmethod
    def unserialize(data):
        raise NotImplementedError


class DataFrameSerializer(SerializerBase):
    @staticmethod
    def serialize(df, to_json=False):
        parser = json if np.any(df.isnull()) else ujson
        if isinstance(df.index, pd.DatetimeIndex):
            df = df.copy()
            df.index = df.index.strftime("%Y-%m-%d %H:%M:%S")
        data = df.to_dict("split")
        if to_json:
            return parser.dumps(data)
        else:
            return data

    @staticmethod
    def unserialize(json_data):
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        df = pd.DataFrame(**data)
        try:
            df.index = pd.to_datetime(df.index)
            df.index.tz=pytz.timezone("Asia/Shanghai")
        except ValueError:
            pass
        return df
