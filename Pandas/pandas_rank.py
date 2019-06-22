import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb

""" 
---- DataFrame 排名
---- 參考書本 P186
---- rank(axis = 0, method='擇一方法')
---- method : avarage (平均值) / min (最小值) / max (最大值) / first (按照數據值相同的元素出現的順序賦予 rank 值) / dense (取最小值，相同元素者構成一組)
"""

db = MySQLdb.connect(host='localhost' , port=3306 , db='pythontest' , user='pythontest' , passwd='pythontest')
df_sql = pd.read_sql('select * from stock limit 50;' , con=db)
db.close()
print(df_sql.head(5))
print('------------')
print(df_sql.head(5).rank(method='average'))

