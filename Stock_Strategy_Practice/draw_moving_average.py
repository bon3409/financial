# -*- coding: UTF-8 -*-

# 繪製價格與 MA 重疊圖表
# 參考課本第 28 個範例

import pandas as pd
from Utilities import Tools
import matplotlib.pyplot as plt

# 使用工具
tools = Tools()

# 股票資訊
code = '2330.TW'
period = '6mo'
interval = '1d'

# MA 週期
cycle = 5

data = tools.getStockDataByYahoo(code, period, interval)
time = data.index.values # 取得時間 (X軸)
closePrice = data.Close.values # 取得收盤價 (Y軸)

MA = tools.getMovingAverageData(code, period, interval, cycle, data)
MaTime = MA.index.values

plt.plot(time, closePrice, label = 'Close Price')
plt.plot(MaTime, MA.MA, label = 'MA')
plt.title(code)
plt.xlabel('Date Time')
plt.ylabel('Price')
plt.legend()
plt.show()