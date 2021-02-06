# 繪製多項次的曲線圖

import numpy as np
import matplotlib.pyplot as plt

# 建立隨機座標
array = [(1, 1), (2, -4), (3, 1), (11, 6), (20, -5), (21,10)]
points = np.array(array)

# get x and y vectors
x = points[:,0]
y = points[:,1]

# 計算多項次方程式
times = len(array) - 1                # 項次的數量
coefficient = np.polyfit(x, y, times) # 產生線性方程式階乘的係數
Formula = np.poly1d(coefficient)      # 多項次的 function

# 計算新的座標(x_new, y_new)，作為繪製曲線的依據
interval = 50 # 將每個座標切分為幾等分，切的越細，曲線會越圓滑
x_new = np.linspace(x[0], x[-1], interval)
y_new = Formula(x_new) # 例如 y=5x^2+x+10 的方程式，把 x 數值帶入，求得 y

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ]) # 設定 x 軸的數值範圍
plt.show()
