import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  # 統計函數的套件

'''
---- 區間估計(Interval Estimation)
---- 使用 scipy 套件中的 t 類別的 interval() 函數進行區間估計
---- interval(alpha, df, loc, scale)
---- alpha : 信心水準(Confidence Level)
---- df : 檢定量的自由度 (degrees of freedom parameter)，需要 n-1 
---- loc : 樣本均值
---- scale : 標準差(在區間估計時，用標準誤來表示樣本標準差)
---- 參考 P284
'''

# 例題一，找出 10 次重量的信賴區間
# 建立 x 樣本 (估計一個物品量測10次的重量)
x = [10.1, 10, 9.8, 10.5, 9.7, 10.1, 9.9, 10.2, 10.3, 9.9]

# 進行區間估計
alpha = 0.95          # 信心水準
df = len(x)-1         # 自由度
loc = np.mean(x)      # 均值
scale = stats.sem(x)  # 在區間估計時，用標準誤來表示樣本標準差

confidence = stats.t.interval(alpha, df, loc, scale)
print('在信心水準95%的情況下，信賴區間為 = ', confidence)
print('------------------------------------')

# 例題二
# 取得數據(緯創2018年日收益率)
stock_3231 = pd.read_csv(r'Statistics\excel\3231\3231緯創_total_info.csv', encoding='utf-8')
stock_3231.index = pd.to_datetime(stock_3231['日期'])
stock_3231_ROI = stock_3231.ROI

# 繪製直方圖
# 確認收益率服從常態分佈
# stock_3231_ROI.astype(np.float).hist()
# plt.show()

# 求出收益率的均值
stock_3231_mean = stock_3231_ROI.mean()

# 求出收益率的標準差
stock_3231_std = stock_3231_ROI.std()

# 進行區間估計
stock_interval = stats.t.interval(0.95, len(stock_3231_ROI)-1, stock_3231_mean, stats.sem(stock_3231_ROI))
print('緯創3231 2018年ROI在95%的信心水準下，信賴區間 = ', stock_interval)