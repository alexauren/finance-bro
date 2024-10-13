import config.config as config
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

class DataCollector():

    def __init__(self):
        self.api_key = config.api_key

    def fetch(self, stock:str, output_format='pandas'):
        ts = TimeSeries(self.api_key, output_format=output_format)
        data, meta = ts.get_daily(stock, outputsize='compact')
        return (data, meta)

    
    def write(self,data, path: str) -> None:
        df = pd.DataFrame(data)
        df.to_csv(f"data/csv/{path}")

dc = DataCollector()
data, meta = dc.fetch('GOOGL')
dc.write(data, 'testfile')