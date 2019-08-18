import pandas as pd
import numpy as np
import ffn

'''
---- 利用 ffn 模組計算收益率，計算單期收益
---- Step 1 : 整理需要使用的數據
---- Step 2 : 利用 to_returns() 取得單期收益率
---- 參考 P339
'''

# 取得股票資料
stock_3231_csv = pd.read_csv(r'D:\Code Training\Python training\financial_excel\3231\3231緯創_total_info.csv', encoding='utf-8')

stock_3231_csv.index = pd.to_datetime(stock_3231_csv['日期'])

close = stock_3231_csv['收盤價']

# 利用 ffn 模組的 to_returns() 計算單期收益率
# 計算結果與原始 excel 表中的 ROI 數據一樣
ffnReturns = ffn.to_returns(close).dropna()
print(ffnReturns.tail(10))

