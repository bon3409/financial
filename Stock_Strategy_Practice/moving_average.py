# -*- coding: UTF-8 -*-

# 逐筆計算移動平均價格(MA)
# 參考課本第 27 個範例

import pandas as pd
from Utilities import Tools

tools = Tools()

# 取得股票資訊
code = '2330.TW'
period = '6mo'
interval = '1d'
data = tools.getStockDataByYahoo(code, period, interval)

# 設定相關變數
ClosePrice = []
Time = []
MAArray = []
MAValue = 0
count = 1
cycle = 5 # 週期(幾日 MA)

for index, row in data.iterrows():
    ClosePrice += [row.Close]
    if (count < cycle):
        count += 1
        continue
    
    segmentTotal = sum(ClosePrice[(count - cycle) : count])
    MAValue = segmentTotal / cycle

    MAArray += [MAValue]
    Time += [index]

    count += 1

MA = pd.DataFrame({'MA': MAArray}, index=Time)
print(MA)
