import ffn
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

'''
---- 利用 ffn 模組直接取得股票資訊 參考: http://pmorissette.github.io/ffn/quick.html
---- 1. 計算單期收益率
---- 2. 計算單期累積收益率
'''

# 取得 3231緯創股票資訊
stock_3231 = ffn.get('3231.TW', start='2018-01-01')
ffnReturn_3231 = ffn.to_returns(stock_3231['3231tw']).dropna()
ffnReturn_3231.name = '3231緯創單期收益率'
annualize_3231 = (1+ffnReturn_3231).cumprod()-1
annualize_3231.name = '3231緯創單期累積收益率'

# 取得 2633台灣高鐵股票資訊
stock_2633 = ffn.get('2633.TW', start='2018-01-01')
ffnReturn_2633 = ffn.to_returns(stock_2633['2633tw']).dropna()
ffnReturn_2633.name = '2633台灣高鐵單期收益率'
annualize_2633 = (1+ffnReturn_2633).cumprod()-1
annualize_2633.name = '2633台灣高鐵單期累積收益率'

# 將資料合併
concat = pd.concat([ffnReturn_3231,ffnReturn_2633, annualize_3231, annualize_2633], axis=1)

# 出圖
matplotlib.use('TkAgg')  # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057
concat.plot()
plt.show()