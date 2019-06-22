import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 資料排序
---- 參考書本 P184
---- sort_values(by='column名稱' , axis = 0 , ascending = True)
---- axis = 0 => 預設值，按照 index 對數據進行排序   axis = 1 => 按照 colume 對數據進行排序
---- ascending = True => 升冪  ascending = False => 降冪
"""

db = MySQLdb.connect(host='localhost' , port=3306 , db='pythontest' , user='pythontest' , passwd='pythontest')
df_sql = pd.read_sql('select * from stock limit 50;' , con=db)
db.close()
print(df_sql.sort_values(by='close_price' , axis=0 , ascending=False))