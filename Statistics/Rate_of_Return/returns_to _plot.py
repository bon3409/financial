import pandas as pd
import numpy as np
import ffn
import matplotlib.pyplot as plt
import matplotlib
import tkinter

'''
---- 利用 ffn 模組計算複利收益率
---- Step 1 : 整理需要使用的數據
---- Step 2 : 利用 to_log_returns() 取得單期收益率
---- 參考 P350
'''

# 取得股票資料
stock_3231_csv = pd.read_csv(r'D:\Code Training\Python training\financial_excel\3231\3231緯創_total_info.csv', encoding='utf-8')

stock_3231_csv.index = pd.to_datetime(stock_3231_csv['日期'])

close = stock_3231_csv['收盤價']

# 利用 ffn 模組的 to_returns() 計算單期收益率
# 計算結果與原始 excel 表中的 ROI 數據一樣
ffnReturns = ffn.to_returns(close).dropna()
ffnReturns.name = '單期收益率'

# 利用 ffn 模組的 to_log_returns() 計算複利收益率
ffnCompoRet = ffn.to_log_returns(close).dropna()
ffnCompoRet.name = '複利收益率'

# 根據單期收益率來計算單期累積收益率
annualize = (1+ffnReturns).cumprod()-1
annualize.name = '單期累積收益率'

# 合併
concat = pd.concat([ffnReturns, ffnCompoRet, annualize], axis=1)
print(concat.tail(5))

# 繪製圖表
matplotlib.use('TkAgg')      # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057
concat.plot()
plt.title('緯創(3231) 收益率比較')
plt.show()