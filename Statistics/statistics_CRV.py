import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  # 統計函數的套件

'''
---- 連續型隨機變數使用
---- 參考 P257
---- 離散型隨機變數(Discrete Random Variable)   : 一個區間內有限制孤立點，例如硬幣正反兩面
---- 連續性隨機變數(Continuous Random Variable) : 一個區間內可以任意取值，例如收益率、價格等等
'''

# # 取得股票 ROE、ROA 資訊
data_list = pd.read_html('https://www.wantgoo.com/stock/report/profit_roe?stockno=3231')   # 取得檔案資料為 list 型態

# 轉換資料型態 list -> dataframe
df = pd.DataFrame(data_list[0])
print(df)

''' 此圖表可以幫助判斷數據分布的狀況，但不能顯示數據的趨勢 '''
''' 曲線的面積等於發生機率(積分的概念) '''
density = stats.gaussian_kde(df['ROE%'])
bins = np.arange(-5,5,0.02)

plt.subplot(211)
plt.plot(bins, density(bins))
plt.title('緯創(3231) ROE 的概率密度曲線')

plt.subplot(212)
plt.plot(bins, density(bins).cumsum())
plt.title('緯創(3231) ROE 累積分布函數圖')
plt.show()


