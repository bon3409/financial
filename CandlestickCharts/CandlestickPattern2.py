import sys
import os
import pandas as pd

# 取得專案目錄
currentDirectory = os.getcwd()

# 將專案目錄加入環境變數，這樣才可以使用別的 package
sys.path.append(currentDirectory)

# 引用別的資料夾寫好的程式
from Tools.StockService import stock

"""
主體: 捕捉 K 線圖的型態
目標: 捕捉「烏雲蓋頂」
參考課本 p535
"""

stock = stock()
Code = 8086
Type = 'two'
startDay = '2020-01-01'

data = stock.getData(Code, Type, startDay)

Close = data.Close
Open = data.Open

# 刻劃捕捉符合「烏雲蓋頂」型態的連續兩根蠟燭實體
Cloud = pd.Series(0, index=data.index)
for i in range(1, len(data)):
    param1 = Close[i] < Open[i]                            # 當天的收盤價低於開盤價 (開高走低)
    param2 = Close[i - 1] > Open[i -1]                     # 前一天的收盤價高於開盤價 (開低走高)
    param3 = Open[i] > Close[i-1]                          # 當天的開盤價大於前一天的收盤價
    param4 = Close[i] < 0.5 * (Close[i - 1] + Open[i - 1]) # 當天的收盤價要小於前一天價格的一半
    parma5 = Close[i] > Open[i - 1]                        # 當天的收盤價要大於前一天的開盤價 (烏雲蓋頂)

    if (param1 and param2 and param3 and param4 and parma5):
        Cloud[i] = 1

# 定義前期上升趨勢 (連續兩天的收益率為正的)
Trend = pd.Series(0, index=Close.index)
for i in range(2, len(Close)):
    if (Close[i-1] > Close[i - 2] > Close[i - 3]):
        Trend[i] = 1

# 尋找「烏雲蓋頂」型態
darkCloud = Cloud + Trend
print(f"股票代號 {Code} 從 {startDay} 開始出現烏雲蓋頂型態的日期:")
print(darkCloud[darkCloud  == 2])