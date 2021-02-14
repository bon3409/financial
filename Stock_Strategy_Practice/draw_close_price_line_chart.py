# -*- coding: UTF-8 -*-

# 繪製價格折線圖
# 參考課本第 25 個範例

from Utilities import Tools
import matplotlib.pyplot as plt

# 以下兩行是解決一些 warning message 用的
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

tools = Tools()

# 取得成交資訊
ticker = '2330.TW'
period = '1mo'
interval = '1d'
data = tools.getStockDataByYahoo(ticker, period, interval)

# 取得時間 (X軸)
time = data.index.values

# 取得收盤價 (Y軸)
closePrice = data.Close.values

# 繪製圖表
plt.plot(time, closePrice)
plt.title(ticker)
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.show()