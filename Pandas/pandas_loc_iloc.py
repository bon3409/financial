import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 索引應用
---- 參考書本 P180
---- DataFrame.loc[row_indexs, column_indexs]     標籤索引
---- DataFrame.iloc[row_indexs, column_indexs]    位置索引
"""
np.random.seed(10)                # 產生同一組隨機數
random_arr = np.random.rand(6,4)  # 產生6*4的矩陣
date = pd.date_range('20190601', periods=6)

original_arr = pd.DataFrame(random_arr, index=date, columns=list('ABCD'))     # 原始資料

print('完整矩陣')
print( original_arr)
print()

# 使用 loc 標籤索引
print('使用 loc 標籤索引')
print(original_arr.loc[:,'A':'C'])
print()

# 使用 iloc 位置索引
print('使用 iloc 位置索引，提取某列')
print(original_arr.iloc[2])
print()

print('使用 iloc 位置索引，提取某行')
print(original_arr.iloc[[1,4],2])
print()

# 取得 column 的資料
print('第一種')
print(original_arr.B)
print()

print('第二種')
print(original_arr['B'])
print()