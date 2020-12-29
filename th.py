from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from matplotlib.pyplot import figure

days = 30

end_date = datetime.today()
start_date = end_date - timedelta(days=days)


def filter_frame(frame):
    result = frame[(frame.index > start_date) & (frame.index <= end_date)]
    result = result.sort_index(ascending=True)
    return result


with open('alphavantage_api_key') as keyfile:
    api_key = keyfile.readline().strip()

ts = TimeSeries(api_key, output_format='pandas')
ti = TechIndicators(api_key, output_format='pandas')

aapl_data, aapl_meta_data = ts.get_intraday(symbol='aapl', outputsize='full')
aapl_bands, aapl_meta_bands = ti.get_bbands(symbol='aapl', interval='daily', time_period=20)
pton_rsi, q = ti.get_rsi(symbol='aapl', interval='daily', time_period=14)

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
# aapl_bands.plot()
# pton_rsi.plot()
# aapl_data['4. close'].plot()
filter_frame(aapl_data)['5. adjusted closed'].plot()

plt.tight_layout()
plt.grid()
plt.savefig('graph.png')
