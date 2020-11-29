# 第一種方法: 作差法求動量質

import os
import sys
import ffn
import itertools
import pandas as pd
import matplotlib.pyplot as plt

# 取得專案目錄
currentDirectory = os.getcwd()

# 將專案目錄加入環境變數，這樣才可以使用別的 package
sys.path.append(currentDirectory)

# 引用別的資料夾寫好的程式
from Tools.StockService import stock

'''
作差法的公式: 今天的價格減去一段時間間隔以前的價格
結論: 如果動量線在 0 的下方，表示正處於下跌趨勢;反之，如果在 0 的上方，表示為上漲趨勢
參考: 書本 P.544
'''

# 取得股票資訊
stock = stock()
Code = 2330
Type = 'tw'
startDay = '2020-01-01'

# 取得股票資料
data = stock.getData(Code, Type, startDay)

# 取得收盤價
Close = data.Close

# 取得滯後五期的收盤價
log5Close = Close.shift(5)

# 計算 5 日動量質
momentum5 = (Close - log5Close).dropna()

# 產生水平線，用於快速區分是上漲還是下跌趨勢
temp = list(itertools.repeat(0, momentum5.size)) # 複製多個相同元素，並且變成 list
HorizontalLine = pd.Series(temp, index=momentum5.index)

# 繪製收盤價與 5 日動量曲線圖
plt.subplot(211)
plt.plot(Close, 'b*')
plt.xlabel('date')
plt.ylabel('Close')
plt.title(f"{Code} Momentum Information")
plt.subplot('212')
plt.plot(momentum5, 'r-*')
plt.plot(HorizontalLine)
plt.xlabel('date')
plt.ylabel('Momentum5')
plt.show()