import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 缺失值 NaN
---- 參考書本 P196
---- isnull()  判斷數據是否為 NaN 值，如果是回傳 True，反之 False
---- notnull() 判斷數據是否為 NaN 值，如果是回傳 False，反之 True
"""

np.random.seed(10)                # 產生同一組隨機數
row1 = ['a','b','c']
row2 = ['b','c','d']

df1 = pd.DataFrame(np.random.rand(3,4), index=row1, columns=list('ABCD'))
df2 = pd.DataFrame(np.random.rand(3,4), index=row2, columns=list('CDEF'))

mul_df = df1.mul(df2, fill_value=0)   # 將兩個矩陣做乘法

print('保留具有數值的數據')
print(mul_df.C[mul_df.C.notnull()])   # 會變成 mul_df.C[[True,True,True,True]]