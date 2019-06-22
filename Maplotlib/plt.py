import pandas as pd
from datetime import datetime
import MySQLdb
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters    # TODO: reason:avoid warnings


""" 
---- 讀取 csv 資料，並做成圖表
---- 參考書本 P204
---- 如果無法顯示 utf-8 時，將 csv 檔案用記事本開啟，並另存格式為 utf-8 即可
"""

df = pd.read_csv('financial\Maplotlib\stock_month_3231.csv', encoding='utf-8')   # read csv file

date = pd.to_datetime(df['日期'])    # the type of index is converted to datetime.datetime

register_matplotlib_converters()     # avoid warning

print(df)   # show the dataframe

plt.figure(dpi=90, figsize=(12,10))   # setting figure size , figure(dpi=N, figsize=(width, height)) , size = N*width , N*height
plt.plot(date, df['收盤價'])
plt.xticks(rotation=45)              # rotate x axis label
plt.xlabel('日期')
plt.ylabel('收盤價')
plt.title('緯創 3231 五月份收盤價資訊')
plt.show()