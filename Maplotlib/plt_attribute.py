import random
import pandas as pd
import numpy as np
from datetime import datetime
import MySQLdb
import matplotlib.pyplot as plt
# from pandas.plotting import register_matplotlib_converters    # TODO: reason:avoid warnings


""" 
---- 修改圖像屬性
---- 參考書本 P206
---- 如果無法顯示 utf-8 時，將 csv 檔案用記事本開啟，並另存格式為 utf-8 即可
"""
# avoid warning
# register_matplotlib_converters()     

plt.figure(dpi=100, figsize=(12, 8))    # setting figure size

# 修該 Matplotlib 函數庫中相關繪圖參數，解決 Y 軸可以顯示負數的問題
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(3,1,1)
plt.plot(np.random.randn(5))
plt.title('這是顯示 Y 軸正負值')

# 調整 XY 座標最大值與最小值
# plt.xlim(min, max)
# plt.ylim(min, max)
plt.subplot(3,1,2)
plt.plot(np.random.rand(5))
plt.ylim(-1.5, 1.5)
plt.title('調整 XY 軸座標範圍值')

# 增加圖形背景 grid (格線)
# plt.grid(True/Flase, axis='y/x/both', which='major/minor/both')
plt.subplot(3,1,3)
plt.plot(np.random.rand(5))
plt.grid(True, axis='y', which='major', )







plt.show()