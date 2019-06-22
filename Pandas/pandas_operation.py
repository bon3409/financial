import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 資料內容操作
---- 參考書本 P189
---- 合併操作 1 => pd.concat([資料1, 資料2,....], axis =1)
---- 合併操作 2 => df.append(新增的資料表格) ，index 與 column 皆會對應到
---- 刪除操作 1 => df.drop('index/欄位名稱', axis = 0/1) ， 不會刪除原 DataFrame
---- 刪除操作 2 => del df['欄位名稱'] ， 刪除原 DataFrame
"""
np.random.seed(10)                # 產生同一組隨機數
random_arr = np.random.random(6)

original_arr = pd.DataFrame({'A':random_arr}, index=pd.date_range('20190601', periods=6))     # 原始資料
add_arr = pd.DataFrame([1,2,3,4,5,6], index=pd.date_range('20190602', periods=6))  # 欲新增的資料欄位

# index 欄位不會新增
# original_arr['B'] = add_arr                
# print('第一種狀況 : \n', original_arr)
# print('------------ 我是分隔線 ------------')


# 統一不同 DataFrame 的 index
new_arr = pd.concat([original_arr, add_arr], axis=1)
print(new_arr)
