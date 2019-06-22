import random
import pandas as pd
import numpy as np
from datetime import datetime

""" 
---- 高低頻時間序列數據轉換
---- 參考書本 P174
"""
np.random.seed(0)             # 產生同一組的隨機數
price = np.random.random(30)   # 產生30個 0~1 的隨機數
date = pd.date_range('20190601', periods=30)     # 建立時間序列

arr = pd.Series(price , index = pd.to_datetime(date))    # 日期與價格的一維陣列

sum_arr = arr.resample('M').sum()      # 將每個月的value 總和在一起
mean_arr = arr.resample('5D').mean()   # 將每5天的 value 平均

print('總和 = \n' , sum_arr , '\n')
print('平均 = \n' , mean_arr , '\n')