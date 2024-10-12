import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class DataCollector():

    def __init__(self):
        self.api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        print(self.api_key)
        # self.api_key = '1MKFCLOIJI3QPW77'

    def fetch(self):
        ts = TimeSeries(self.api_key, output_format='pandas')
        data, meta = ts.get_intraday('TSLA', interval='1min', outputsize='full')
        print(data, meta)
    
dc = DataCollector()
dc.fetch()