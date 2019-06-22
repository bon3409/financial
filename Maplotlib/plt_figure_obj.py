import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb
import matplotlib.pyplot as plt

""" 
---- Figure、Axes 物件
---- 參考書本 P234
---- 
"""

# 建立 figure 物件
fig = plt.figure()

# 建立 Axes 物件，可以指定位置與大小
# add_axes([a, b, c, d])  => (a,b)為物件左下角座標點，(c,d)分別為 X 與 Y 軸方向的長度
ax1 = fig.add_axes([0.1, 0.1, 0.3, 0.3])
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

# 建立亂數 array
arr = np.random.randn(5)

# 設定顯示內容，前綴字 : set_
ax1.plot(arr)
ax1.set_title('這是 ax1')
ax1.set_xlabel('這是 X 軸標籤')
ax1.set_ylabel('這是 Y 軸標籤')
ax1.set_ylim(-1,1)

ax2.plot(arr)
plt.show()