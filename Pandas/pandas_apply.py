import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 函數應用和映射
---- 參考書本 P195
---- DataFrame.apply(function, axis=0/1)
"""
np.random.seed(10)                # 產生同一組隨機數
random_arr = np.random.rand(6,4)  # 產生6*4的矩陣
date = pd.date_range('20190601', periods=6)

original_arr = pd.DataFrame(random_arr, index=date, columns=list('ABCD'))     # 原始資料

# 在矩陣中找出最大值
max_arr = original_arr.apply(max, axis=1)

# 在矩陣中找出最小值
min_arr = original_arr.apply(min, axis=1)


print('找出最大值\n', max_arr)
print()
print('找出最小值\n', min_arr)