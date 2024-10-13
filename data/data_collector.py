import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd


class DataCollector():

    def __init__(self):
        self.api_key = '1MKFCLOIJI3QPW77' # Not the actual api key of course, that would be bad practice. I would never do that. 

    def fetch(self, stock:str, interval: str, output_format='pandas'):
        ts = TimeSeries(self.api_key, output_format=output_format)
        data, meta = ts.get_intraday(stock, interval=interval, outputsize='full')
        return (data, meta)
    
    def write(self,data, path: str) -> None:
        df = pd.DataFrame(data)
        df.to_csv(f"data/csv/{path}")

dc = DataCollector()
data, meta = dc.fetch('TSLA', '1min')
dc.write(data, 'testfile')