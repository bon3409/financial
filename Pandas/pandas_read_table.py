import random
import pandas as pd
import numpy as np
from datetime import datetime

""" 
---- read_table 處理 .txt / .csv 等檔案
---- 參考書本 P176
"""

df = pd.read_table('financial\Pandas\stock_3231.csv' , sep=',' , encoding='utf-8')

print(df)