import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 將缺失值填滿
---- 參考書本 P198
---- fillna(value=None, method=None, axis=None, inplace=False, limit=None)
---- value = 要填滿的值，數字或字串皆可
---- mehtod = ffill/pad       (用行或列方向的上一個觀測值來填滿)
---- method = bfill/backfill  (用行或列方向的下一個觀測值來填滿)
---- axis = 0(index)/1(column)  搭配 method 使用
---- inplace = True  (顛倒 DataFrame)
---- inplace = False (預設，維持原本 DataFrame 形式)
---- limit = N  (指定連續 N 個數值填滿)
"""

np.random.seed(10)                # 產生同一組隨機數
row1 = ['a','b','c']
row2 = ['b','c','d']

df1 = pd.DataFrame(np.random.rand(3,4), index=row1, columns=list('ABCD'))
df2 = pd.DataFrame(np.random.rand(3,4), index=row2, columns=list('CDEF'))

mul_df = df1.mul(df2)   # 將兩個矩陣做乘法

print('原始數據')
print(mul_df)
print()

# 將 NaN 值轉換成其他值/字串
print('將 NaN 值轉換成其他值')
print(mul_df.fillna(value='string'))
print()

# 用同一個 column 前一個觀測值填滿，axis = 0 (index)
print('用同一個 column 前一個觀測值填滿，axis = 0 (index)')
print(mul_df.fillna(method='ffill', axis=0))
print()

# 用同一個 row 前一個觀測值填滿
print('用同一個 row 後一個觀測值填滿')
print(mul_df.fillna(method='backfill'))
print()

# 連續 NaN 值時，按照 limit 指定個進行填滿
print('連續 NaN 值時，按照 limit 指定個進行填滿')
print(mul_df.fillna(method='pad', limit=2))
print()