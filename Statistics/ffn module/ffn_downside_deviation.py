import ffn

'''
---- 下檔風險來衡量風險
---- 跌勢差法 (Downside Deviation) : 說明「最低可以接受的收益率」(Minimnm Acceptable Rate of Teturn，MARR) 的發散程度
---- 參考 P.360
'''

# 取得 股票資訊
def getStockInfo(stock_code):
    full_code_name = str(stock_code) + '.TW'
    return ffn.get(full_code_name, start='2019-01-01')

# 取得 單期收益率
def getReturn(datafarm):
    return ffn.to_returns(datafarm).dropna()

# 計算跌勢差，運用到『平均絕對偏差』的概念，參考 P.252
# 公式 : δ(R,MARR)=\sqrt(1/T\ \sum_(t=1)^T\of\begin[\min\funcapply(R-MARR,0)]〗^2 )  參考 P360

def cal_half_dev(returns):
    mean_return = returns.mean()                            # 取得單期收益率的平均值
    temp = returns[returns<mean_return]                     # 取得小於單期收益率小於平均值的 dataframe

    half_deviation = ((((mean_return - temp)**2).dropna()).sum()/len(returns))**0.5    # 計算下檔風險值
    return (half_deviation)

print('比較各股的『下檔風險值』 : ')
print(cal_half_dev(getReturn(getStockInfo(3231))), '\n')
print(cal_half_dev(getReturn(getStockInfo(2633))), '\n')
print(cal_half_dev(getReturn(getStockInfo(3702))), '\n')
print(cal_half_dev(getReturn(getStockInfo(2376))), '\n')
print(cal_half_dev(getReturn(getStockInfo(2330))), '\n')
print(cal_half_dev(getReturn(getStockInfo('0056'))), '\n')
