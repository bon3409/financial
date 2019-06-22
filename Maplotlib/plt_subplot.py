import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters    # TODO: reason:avoid warnings

""" 
---- Figure、Axes 物件
---- 參考書本 P234
---- 
"""
register_matplotlib_converters()     # avoid warning

df = pd.read_csv('financial\Maplotlib\stock_month_3231.csv', encoding='utf-8')   # read csv file
date = pd.to_datetime(df['日期'])
print(df)
plt.figure(dpi=90, figsize=(12,10))

# 建立表格 1
ax1 = plt.subplot(2,1,1)
ax1.plot(date, df['收盤價'])
ax1.set_title('緯創 3231 五月份走勢圖')

# 建立表格 2
ax2 = plt.subplot(2, 1, 2)
ax2.bar(date, df['成交筆數'], color='blue')
ax2.set_title('成交筆數')
plt.show()

