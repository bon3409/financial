import ffn
from scipy.stats import norm

# 取得 股票單期收益率資訊
def getStockReturnInfo(stock_code):
    full_code_name = str(stock_code) + '.TW'
    stock_info = ffn.get(full_code_name, start='2019-01-01')
    return ffn.to_returns(stock_info).dropna()


# 歷史模擬法(Historical Simulation Approach)
# 依照過去歷史作為依據來預測，不適合預測現今變數很多的中美貿易戰期間
# .quantile(α) 取得 α 的分位數，(1-α%) 叫做 VaR 的信心水準

print('以下為歷史模擬法的數據 :')
print('3231 = ', getStockReturnInfo(3231).quantile(0.05).values[0]*100)
print('2633 = ', getStockReturnInfo(2633).quantile(0.05).values[0]*100)
print('3702 = ', getStockReturnInfo(3702).quantile(0.05).values[0]*100)
print('2376 = ', getStockReturnInfo(2376).quantile(0.05).values[0]*100)
print('0056 = ', getStockReturnInfo('0056').quantile(0.05).values[0]*100)
print('===================================')

# 共變異數矩陣法 (Variance-Covariance Approach)
# 假設 (1)資產的收益率服從常態分佈，(2)投資組合的收益率與資產的收益率成線性關係
# 也是依賴歷史資料，對於極端事件的預測能力較差
# norm.ppf(機率水平, 均值, 標準差)

print('以下為共變異數矩陣法的數據 :')
print('3231 = ', norm.ppf(0.05,getStockReturnInfo(3231).mean() , getStockReturnInfo(3231).std())[0]*100)
print('2633 = ', norm.ppf(0.05,getStockReturnInfo(2633).mean() , getStockReturnInfo(2633).std())[0]*100)
print('3702 = ', norm.ppf(0.05,getStockReturnInfo(3702).mean() , getStockReturnInfo(3702).std())[0]*100)
print('2376 = ', norm.ppf(0.05,getStockReturnInfo(2376).mean() , getStockReturnInfo(2376).std())[0]*100)
print('0056 = ', norm.ppf(0.05,getStockReturnInfo('0056').mean() , getStockReturnInfo('0056').std())[0]*100)