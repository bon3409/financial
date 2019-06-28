import numpy as np
import random
import pandas as pd
from scipy import stats  # 統計函數的套件

'''
---- 常態分布(Normal Distribution)，又稱高斯分布(Gaussian Distribution)
---- 參考 P264
'''

# 產生 N 個常態分佈隨機數
# np.random.normal(size, loc=0.0, scale=1.0)
# size = 表示產生的隨機數數量
# loc = 表示常態分佈的均值
# scale = 表示常態分佈的標準差，default = 1
N = 5
norm = np.random.normal(size=N)
print('產生 {} 個常態分布隨機數'.format(N), norm)
print('----------------------------')

# 取得常態分佈隨機數的密度值
prob_arr = stats.norm.pdf(norm)
print('常態分佈隨機數密度值 = ', prob_arr)
print('----------------------------')

# 取得常態分佈隨機數得累積密度值
stack_arr = stats.norm.cdf(norm)
print('常態分佈隨機數得累積密度值 = ', stack_arr)
print('----------------------------')

'''
# 常態分佈在金融市場的應用 VaR (Value at Risk)
# VaR : 指的是在一定的機率水平(α%)下，某一金融資產或金融資產組合在未來特定一段時間內的最大可能損失
# (1-α%) 叫做 VaR 的信心水準
# 前提 : 假設收益率序列為常態分佈
# stats.norm.ppf(機率水平, 均值, 標準差)
'''

# 取得 ROI 的資料
ret = pd.read_csv('excel\Statistics\stock_2633.csv')['ROI'].tail(21)   # 扣除掉第一個ROI為0的數據

# 取得收益率序列的均值
ret_mean =ret.mean()

# 取得標準差
ret_std = ret.std()

# 查詢累積密度值為 0.05 的分位數
α = 0.05
VaR = stats.norm.ppf(α, ret_mean, ret_std)
condifince = 1 - α
print('有 {}% 的機率損失不會超過 = '.format(condifince), abs(round(VaR, 2)), '%')
