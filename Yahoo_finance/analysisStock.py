# 1. 將取得的股票資訊收盤價轉換成曲線
# 2. 抓到斜率接近於 0 的位置(價格)，表示這邊為趨勢反轉的關鍵價格
# 3. 取得收盤價的平均值
# 4. 判斷趨勢反轉的點跟平均值的相對位置，建立壓力支撐線
# 5. 判斷當前的曲線圖是否符合標準圖 maybe use openCV，參考 https://kknews.cc/zh-tw/tech/x6le588.html
# 6. 符合標準圖，用 Line 通知

import sys
import numpy as np
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt

# 取得股瞟資訊
def getStock(codes, period = '1mo', interval = '1d'):
    try:
        tickers = ''
        for code in codes:
            tickers = tickers + ' ' + code

        if ('TWO' in tickers or 'two' in tickers):
            if (period == '1d'):
                raise Exception('上櫃股票的時間區間至少為兩天')

            if(interval in ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h']):
                raise Exception('上櫃股票的 k 線間隔至少要日線以上')

        data = yf.download(tickers=tickers, period=period, interval=interval)

        return data
    except Exception  as e:
        print(e)
        sys.exit(1) # exiing with a non zero value is better for returning from an error    

codes = ['2330.TW']
data = getStock(codes, period='30d', interval='30m')

# ==============
# 計算平均值
# ==============
averageClosePrice = round(data['Close'].mean(), 2)
print(f"平均值: {averageClosePrice}")

closePriceArray = data['Close'].values.tolist()

array = list(enumerate(closePriceArray))
points = np.array(array)

x = points[:,0]
y = points[:,1]

# 計算多項次方程式
times = len(array) - 1                # 項次的數量
coefficient = np.polyfit(x, y, 18) # 產生線性方程式階乘的係數
Formula = np.poly1d(coefficient)      # 多項次的 function

# 計算新的座標(x_new, y_new)，作為繪製曲線的依據
interval = 1000 # 將每個座標切分為幾等分，切的越細，曲線會越圓滑
x_new = np.linspace(x[0], x[-1], interval)
y_new = Formula(x_new) # 例如 y=5x^2+x+10 的方程式，把 x 數值帶入，求得 y

# ====================
# 取得斜率等於 0 的數值
# ====================
peaks = []
for i, (xPoint, yPoint) in enumerate(zip(x_new, y_new)):
    status = True
    if i < 3:
        continue
    
    # 斜率計算: y2-y1 / x2-x1
    slope_old = (y_new[i - 2] - y_new[i - 1]) / (x_new[i - 2] - x_new[i - 1])
    slope_new = (y_new[i - 1] - yPoint) / (x_new[i - 1] - xPoint)

    # 紀錄斜率改變的點 (peak)
    if (slope_old * slope_new < 0):
        peaks.append(yPoint)

# ==============
# 建立壓力/支撐線
# ==============
pressures = []
supports = []
for price in peaks:
    if price > averageClosePrice:
        pressures.append(price)
    else:
        supports.append(price)

print(f"壓力: {pressures}")
print(f"支撐: {supports}")

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ]) # 設定 x 軸的數值範圍
plt.show()
