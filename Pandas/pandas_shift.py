import random
import pandas as pd
import numpy as np
from datetime import datetime

""" 
---- 滯後或者超前操作
---- 計算單期收益率
---- 參考書本 P173~174
"""

price = [20.34,20.56,21.01,20.65,21.34]
date = pd.date_range('20190601', periods=5)     # 建立時間序列

arr = pd.Series(price , index = pd.to_datetime(date))    # 日期與價格的一維陣列

# 計算單期收益率
rate = (arr - arr.shift(1)) / arr.shift(1)
print(rate)