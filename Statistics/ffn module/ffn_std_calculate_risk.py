import ffn
import matplotlib
import matplotlib.pyplot as plt

'''
---- 資產風險的測度
---- 利用變異數(標準差)來評估風險
---- 參考 P359
'''

# get stock info
stock_3231 = ffn.get('3231.TW', start='2019-01-01')
stock_2633 = ffn.get('2633.TW', start='2019-01-01')
stock_3702 = ffn.get('3702.TW', start='2019-01-01')
stock_2834 = ffn.get('2834.TW', start='2019-01-01')
stock_2376 = ffn.get('2376.TW', start='2019-01-01')

# 計算單期收益率
stock_3231_return = ffn.to_returns(stock_3231).dropna()
stock_2633_return = ffn.to_returns(stock_2633).dropna()
stock_3702_return = ffn.to_returns(stock_3702).dropna()
stock_2834_return = ffn.to_returns(stock_2834).dropna()
stock_2376_return = ffn.to_returns(stock_2376).dropna()

# 計算變異數(標準差)，來簡單評估風險
std_3231 = stock_3231_return.std()
std_2633 = stock_2633_return.std()
std_3702 = stock_3702_return.std()
std_2834 = stock_2834_return.std()
std_2376 = stock_2376_return.std()

# 比較各支股票的變異數
print('變異數的大小，可以簡單比較出股票之間的風險大小')
print('3231 緯創 : ', std_3231 , '\n')
print('2633 台灣高鐵 : ', std_2633, '\n')
print('3702 大聯大 : ', std_3702 , '\n')
print('2834 臺企銀 : ', std_2834 , '\n')
print('2376 技嘉 : ', std_2376 , '\n')
