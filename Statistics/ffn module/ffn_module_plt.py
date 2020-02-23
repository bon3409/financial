import pandas as pd
import ffn
import matplotlib
import matplotlib.pyplot as plt

'''
---- 利用 ffn 模組出圖
'''

def getStockInfo(stock_name, start_date=None):
    ''' get stock info from yahoo finamce'''
    return ffn.get(stock_name, start=start_date)

def getStockReturnsInfo(stock_frame):
    '''取得股票收益率'''
    return ffn.to_returns(stock_frame)

def getAnnualize(stock_returns):
    '''取得股票累積收益率'''
    return (1 + stock_returns).cumprod() - 1

# 出圖
matplotlib.use('TkAgg')  # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057

stock_twii = getAnnualize(getStockReturnsInfo(getStockInfo('^twii', '2018-01-01')))
stock_3231 = getAnnualize(getStockReturnsInfo(getStockInfo('3231.tw', '2018-01-01')))
stock_2633 = getAnnualize(getStockReturnsInfo(getStockInfo('2633.tw', '2018-01-01')))
stock_3702 = getAnnualize(getStockReturnsInfo(getStockInfo('3702.tw', '2018-01-01')))
stock_2376 = getAnnualize(getStockReturnsInfo(getStockInfo('2376.tw', '2018-01-01')))
stock_2408 = getAnnualize(getStockReturnsInfo(getStockInfo('2408.tw', '2018-01-01')))
stock_1605 = getAnnualize(getStockReturnsInfo(getStockInfo('1605.tw', '2018-01-01')))
stock_0056 = getAnnualize(getStockReturnsInfo(getStockInfo('0056.tw', '2018-01-01')))
stock_0050 = getAnnualize(getStockReturnsInfo(getStockInfo('0050.tw', '2018-01-01')))
stock_00850 = getAnnualize(getStockReturnsInfo(getStockInfo('00850.tw', '2018-01-01')))

concat = pd.concat([
    stock_twii,
    stock_3231,
    stock_2633,
    stock_3702,
    stock_2376,
    stock_2408,
    stock_1605,
    stock_0056,
    stock_0050,
    stock_00850
], axis=1)

# 收益率
concat.plot()

# 關係熱圖
concat.plot_corr_heatmap()

# 虧損幅度
concat.to_drawdown_series().plot()
plt.show()