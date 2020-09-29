import pandas as pd
import ffn
import matplotlib
import matplotlib.pyplot as plt
import ffn_utility as utility

# 出圖
matplotlib.use('TkAgg')  # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057

stock_array = ['^twii', '3231.tw', '2633.tw', '3702.tw', '2330.tw', '2408.tw']
appended_data = []

# 取得個股累積收益率
for stock in stock_array:
    stock_return = utility.getAnnualize(stock, start_date='2017-01-01')
    appended_data.append(stock_return)

concat = pd.concat(appended_data, axis=1)

# 求共變異數矩陣(用來判斷兩個變數間的相關性)
cov_mat = concat.cov()

concat.plot()
plt.show()


