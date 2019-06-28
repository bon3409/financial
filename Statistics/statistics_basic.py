import pandas as pd

'''
---- 基礎統計學
---- 參考 P248
'''

stock_3231 = pd.read_csv('financial\Statistics\excel\stock_month_3231.csv' , encoding='utf-8')

# 以下以 收盤價 作為數據分析項目
close_price = stock_3231['收盤價']

# 取得平均數
close_mean = close_price.mean()

# 取得中位數
close_median = close_price.median()

# 取得眾數
# type = <class 'pandas.core.series.Series'>
close_mode = close_price.mode()

# 取得四分位數
arr = [0.25, 0.5, 0.75]
close_quantile = []
for i in arr:
    close_quantile.append(close_price.quantile(i))

# 取得數據離散的全距
# 最大值(max) - 最小值(min)
close_gap = close_price.max() - close_price.min()

# 取得平均絕對偏差
close_mad = close_price.mad()

# 取得變異數
close_var = close_price.var()

# 取得標準差
close_std = close_price.std()

print('收盤價平均數 = ', close_mean)
print('收盤價中位數 = ', close_median)
print('收盤價眾數   = ', close_mode[0])
print('收盤四分位數  = ', close_quantile)
print('---------------------------------')
print('全距  = ', close_gap)
print('平均絕對偏差  = ', close_mad)
print('變異數  = ', close_var)
print('標準差  = ', close_std)

print('---------------')
print('使用 describe 顯示數據')
print(close_price.describe())