import pandas as pd
import numpy as np

'''
---- 離散型隨機變數使用
---- 參考 P255
---- 離散型隨機變數(Discrete Random Variable)   : 一個區間內有限制孤立點，例如硬幣正反兩面
---- 連續性隨機變數(Continuous Random Variable) : 一個區間內可以任意取值，例如收益率、價格等等
'''
# 產生隨機變數
# np.random.choice(a, size=None, replace=True, p=None)
# a = 隨機變數所有可能的取值
# size = 產生隨機陣列的大小，int or tuple of ints
# replace = boolean, Whether the sample is with or without replacement
# p = 為一個與 X 等長的向量，指定了每種結果出現的可能性，"a"每個項目出現的機率，加起來等於1
arr = [1, 2, 3, 4, 5]
p = [0.1, 0.1, 0.3, 0.3, 0.2]
random_num = np.random.choice(arr, size=10, replace=True, p = p)

print('概率質量函數的隨機數')
print(random_num)
print()

# 將產生的隨機數轉換成 Series ，並記錄出現次數
random_count = pd.Series(random_num).value_counts()
print('頻數分布狀況')
print(random_count)
print()

# 計算頻率分布
random_freq = pd.Series(random_num).value_counts()/100
print('頻率分布狀況')
print(random_freq)
