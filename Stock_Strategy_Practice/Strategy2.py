# -*- coding: UTF-8 -*-

# 歷史策略回測 - 價格突破區間順勢策略 (適用於趨勢盤)
# 參考課本第 45 個範例

"""
小結:
此策略每天最多只會有一次進場的機會
如果價格波動大，一樣只會有第一筆出發條件的進場紀錄
"""

import pandas as pd
from Utilities import Tools
import matplotlib.pyplot as plt

tools = Tools()

code = '2330.TW'
period = '1mo'
interval = '30m'
data = tools.getStockDataByYahoo(code, period, interval)

# 策略需要的參數
boxRatio = 0.02 # 設定區間，如果超過開盤價的這個區間，就做多;反之跌破區間，就做空
stopLossRation = 0.015 # 停損點比例
stopLossPoint = None # 停損點
takeProfitRatio = 0.07 # 停利點比例
takeProfitPoint = None # 停利點
totalProfit = 0 # 定義績效
entryPrice = 0 # 進場價格
exitPrice = 0 # 出場價格
tradeCount = 0
noTradeCount = 0

# 依照 index 的年、月、日做 groupby
# 參考: https://stackoverflow.com/a/35489937
groupByData = data.groupby([data.index.year, data.index.month, data.index.day])

# 針對 groupby 的資料做回測
# 參考 https://realpython.com/pandas-groupby/#how-pandas-groupby-works
for date, rows in groupByData:
    isFirstRow = False # 判斷是否為當天第一筆交易
    index = 0 # 判斷今天是否有執行交易
    openPrice = 0
    totalCount = 0 # 用於比對是否當天的交易都做完了

    for row in rows.iterrows():
        totalCount += 1

        if (isFirstRow is not True):
            # 是開盤價的情況
            isFirstRow = True
            openPrice = row[1]['Open']

        # 建立價格區間
        upperLimit = openPrice * (1 + boxRatio)
        lowerLimit = openPrice * (1 - boxRatio)

        # 進場的判斷
        price = row[1]['Open']
        
        # 當價格突破上界(做多)
        if price >= upperLimit:
            index = 1
            entryPrice = price
            stopLossPoint = openPrice * (1 - stopLossRation)
            takeProfitPoint = openPrice * (1 + takeProfitRatio)
            tradeCount += 1
            break
        # 當價格突破下界(做空)
        elif price <= lowerLimit:
            index = -1
            entryPrice = price
            stopLossPoint = openPrice * (1 + stopLossRation)
            takeProfitPoint = openPrice * (1 - takeProfitRatio)
            tradeCount += 1
            break
        # 當天尚未交易
        elif totalCount == len(rows) - 1:
            noTradeCount += 1
            print(f"{date} 並未交易")

    # 如果今天沒有交易，就不需要做出場的判斷
    if index == 0:
        continue

    skipCount = 0

    # 做多出場
    if index == 1:
        for row in rows.iterrows():
            skipCount += 1
            if skipCount <= totalCount:
                continue

            price2 = row[1]['Open']

            # 停損判斷
            if price2 <= stopLossPoint:
                exitPrice = price2
                break
            # 停利判斷
            elif price2 >= takeProfitPoint:
                exitPrice = price2
                break
            # 收盤強制出場
            elif skipCount == len(rows) - 1:
                exitPrice = price2

        profit = exitPrice - entryPrice
        totalProfit += profit
    
    # 做空出場
    elif index == -1:
        for row in rows.iterrows():
            skipCount += 1
            if skipCount <= totalCount:
                continue

            price2 = row[1]['Open']

            # 停損判斷
            if price2 >= stopLossPoint:
                exitPrice = price2
                break
            # 停利判斷
            elif price2 <= takeProfitPoint:
                exitPrice = price2
                break
            # 收盤強制出場
            elif skipCount == len(rows) - 1:
                exitPrice = price2

        profit = exitPrice - entryPrice
        totalProfit += profit

print(f"    交易天數: {tradeCount}")
print(f"沒有交易次數: {noTradeCount}")
print(f"      總收益: {totalProfit}")