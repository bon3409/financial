import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- 讀取 MySQL 資料
---- 參考書本 P176
---- 需安裝 pip install mysqlclient
---- 需安裝 piip install SQLAchemy
---- MySQLdb.connect(host='localhost' , port=3306 , db='資料庫名稱' , user='帳號名稱' , passwd='密碼')
---- pd.read_sql('select * from 資料表名稱 limit 讀取資料筆數;' , con=資料庫名稱')
"""

db = MySQLdb.connect(host='localhost' , port=3306 , db='pythontest' , user='pythontest' , passwd='pythontest')
df_sql = pd.read_sql('select * from stock limit 50;' , con=db)
db.close()
# print(df_sql)

print(df_sql.close_price)