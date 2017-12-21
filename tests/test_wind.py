import unittest
from quant.data import wind


class WindTestCase(unittest.TestCase):
    def test_get_stock_st(self):
        st = wind.get_stock_st()
        st_table = wind.get_wind_table("AShareST")
        for _, row in st_table.iterrows():
            key = row.s_info_windcode
            if key not in st.columns:
                continue
            start = row.entry_dt
            end = row.remove_dt
            self.assertTrue(st.loc[start:end, key].all())

