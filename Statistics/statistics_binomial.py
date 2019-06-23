import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  # 統計函數的套件

'''
---- 二項分布 (重複 n 次的伯努力試驗)
---- 伯努力試驗的結果只有成功(關注的項目)與失敗(不關注的項目)兩種
---- 參考 P261
'''

# 產生 20 個來源於二項分布的隨機數
n = 100     # 表示伯努力試驗的次數
p = 0.5     # 表示伯努力成功的機率
size = 20   # 表示產生的隨機數的數量
random_arr = np.random.binomial(n, p, size)
print('產生{}個隨機變數 = '.format(size),random_arr)
print('------------------------')


# 計算二項分布的機率質量函數
'''
例題1: 投擲硬幣出現正面的機率為 0.5，投擲100次，出現20次為正面的機率為多少 ?
sol: (C100取20)*(1/2)^20*(1/2)^80
解釋: (20次正面的排列組合)*[(是正面的機率)^正面的次數]*[(不是正面的機率)^不是正面的次數]
'''
# 使用 stats.binom.pmf(條件狀況, 執行次數, 獨立事件的機率)
# PMF = Probability Mass Function 機率質量函數
probability_1 = stats.binom.pmf(20, 100, 0.5)
print('投擲硬幣出現正面的機率為 0.5，投擲100次，出現20次的機率為 = ',probability_1)
print('------------------------')


'''
例題2 : 擲骰子出現 6 的機率為 1/6，投擲100次，出現30次為6的機率為多少?
sol: (C100取30)*(1/6)^30*(1/6)^70
解釋: (30次骰出6的組合)*[(骰出6的機率)^骰出6的次數]*[(骰出不是6的機率)^骰出不是6的次數]
'''
probability_2 = stats.binom.pmf(30, 100, 0.166667)
print('擲骰子出現 6 的機率為 1/6，投擲100次，出現30次為6的機率為多 = ',probability_2)
print('------------------------')


# 計算二項分布累積分布函數
'''
例題3: 投擲硬幣出現正面的機率為 0.5，投擲100次，出現小於等於20次為正面的機率為多少 ?
'''
# 第一種方法
contition = np.arange(0, 21, 1)    # 表示 : [0,1,2,3.....19,20] 小於等於20次的正面次數
arr = stats.binom.pmf(contition, 100, 0.5)
probability_3 = arr.sum()
print('投擲硬幣出現正面的機率為 0.5，投擲100次，出現小於等於20次為正面的機率為多 = ', probability_3)
print('------------------------')

# 第二種方法
# stats.binom.cdf(小於等於某條件, 執行次數, 獨立事件的機率)
probability_4 = stats.binom.cdf(20, 100, 0.5)
print('投擲硬幣出現正面的機率為 0.5，投擲100次，出現小於等於20次為正面的機率為多 = ', probability_4)
print('------------------------')


# 二項分布在金融市場的應用
roi = pd.read_csv('Statistics\stock_2633.csv')
ROI = roi['ROI']
count = len(ROI)               # 總數
rise_count = len(ROI[ROI>0])   # 上漲的數量
p = rise_count/count           # 上漲機率

'''
例題 : 估計 N 個交易日中，有 K 個交易日中上漲的機率為多少
'''
N = 10
K = 5
probability_5 = stats.binom.pmf(K, N, p)
print('估計 {} 個交易日中，有 {} 個交易日中上漲的機率為 = '.format(N, K), probability_5)
print('------------------------')

'''
例題 : 估計 N 個交易日中，小於等於 K 個交易日中上漲的機率為多少
'''
N = 10
K = 5
probability_6 = stats.binom.cdf(K, N, p)
print('估計 {} 個交易日中，小於等於 {} 個交易日中上漲的機率為 = '.format(N, K), probability_6)