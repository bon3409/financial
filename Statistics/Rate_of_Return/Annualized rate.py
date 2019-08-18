import pandas as pd
import numpy as np
import ffn

'''
---- 利用 ffn 模組計算年化收益率
---- Step 1 : 整理需要使用的數據
---- Step 2 : 利用 to_returns() 取得單期收益率
---- Step 3 : 根據單期收益率計算年化收益率
---- 參考 P339
'''

# 取得股票資料
stock_3231_csv = pd.read_csv(r'D:\Code Training\Python training\financial_excel\3231\3231緯創_total_info.csv', encoding='utf-8')

stock_3231_csv.index = pd.to_datetime(stock_3231_csv['日期'])

close = stock_3231_csv['收盤價']

# 利用 ffn 模組的 to_returns() 計算單期收益率
ffnReturns = ffn.to_returns(close).dropna()

# 年化收益率計算
# 投資人持有資產時間為 T 期
# 一年共有 M 期
# 年化收益率公式 : {[(1+r1)(1+r2)...(1+rN)]**(1/(T/M))}-1
# .cumprod() => 將 array 中的值累乘積

'''
需特別注意的地方:
公式中的次方為 (1/(T/M)) ，可以簡化成 (M/T)，公式即變成 : {[(1+r1)(1+r2)...(1+rN)]**(M/T)}-1
'''
# 假設一年有245個交易日
annualize = (1+ffnReturns).cumprod()[-1]**(245/311)-1
 
print(annualize)

