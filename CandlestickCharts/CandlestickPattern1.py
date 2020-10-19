import ffn
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from cycler import cycler # 用於制定線條顏色
import mplfinance as mpf

"""
主體: 捕捉 K 線圖的型態
目標: 捕捉「早晨之星」
參考課本 p530
"""

def getStockData(stock: int, startDay: str):
    """取得指定股票的交易資訊

    Args:
        stock (int): 股票代號
        startDay (str): 開始交易日期
    """
    data = ffn.get(f"{stock}.TW:Open, {stock}.TW:High, {stock}.TW:Low, {stock}.TW:Close", start=startDay)

    # 取得時間(date)，並加入 DataFrame 之中，而且要排在第一欄，為了之後畫 K 線圖
    floteDate = data.index.to_pydatetime()
    data.insert(0, "Date", floteDate)

    # 變更欄位名稱
    data = data.rename(columns={f"{stock}twopen": 'Open', f"{stock}twhigh": 'High', f"{stock}twlow": 'Low', f"{stock}twclose": 'Close'})

    return data

def getDiffPriceData(data):
    closePrice = data.Close # 收盤價
    openPrice = data.Open   # 開盤價

    diffPrice = closePrice - openPrice # 計算每一個交易日的收盤價與開盤價的差異值

    return diffPrice




# 開始執行程式
data = getStockData(3231, '2020-01-01')

diffPrice = getDiffPriceData(data)

# 條件一: 捕捉綠色實體、十字星和紅色實體
Shape = [0, 0, 0]
for i in range(3, len(diffPrice)):
    param1 = diffPrice[i - 2] < 0                            # 前兩天的收盤價要低於開盤價 (開高走低)
    param2 = abs(diffPrice[i - 1]) < 20                      # 第一天的收盤價與開盤價大致相等，在一個指定的區間內
    param3 = diffPrice[i] > 0                                # 當天的收盤價高於開盤價 (開低走高)
    param4 = abs(diffPrice[i] > abs(diffPrice[i - 2] * 0.5)) # 當天的價差要大於前兩天的價差的一半

    if (param1 and param2 and param3 and param4):
        Shape.append(1)
    else:
        Shape.append(0)

# 條件二: 捕捉符合十字星位置的蠟燭圖
Doji = [0, 0, 0]
for i in range(3, len(data.Open)):
    param1 = data.Open[i - 1] < data.Open[i]
    param2 = data.Open[i - 1]< data.Close[i - 2]
    param3 = data.Close[i - 1] < data.Open[i]
    param4 = data.Close[i - 1] < data.Close[i - 2]

    if (param1 and param2 and param3 and param4):
        Doji.append(1)
    else:
        Doji.append(0)

# 條件三: 尋找向下趨勢
Trend = [0, 0, 0]
for i in range(3, len(data.Close)):
    if data.Close[i - 2] < data.Close[i - 3]:
        Trend.append(1)
    else:
        Trend.append(0)

# 以上三個條件畫完之後，用 Python 開始尋找「早晨之星」

StarSig = []
for i in range(len(Trend)):
    if all([Shape[i] == 1, Doji[i] == 1, Trend[i] == 1]):
        StarSig.append(1)
        # 這邊找到的時間點是「早晨之星」圖形第三天的時間點
        print(f"出現早晨之星的時間: {data.index[i]}")
    else:
        StarSig.append(0)

