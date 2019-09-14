import ffn

'''
---- 利用 ffn 模組計算風險最大虧損
---- 參考 P.368
---- .cumprod()  計算累積收益率
'''

# 取得 股票單期收益率資訊
def getStockReturnInfo(stock_code):
    full_code_name = str(stock_code) + '.TW'
    stock_info = ffn.get(full_code_name, start='2019-01-01')
    return ffn.to_returns(stock_info).dropna()

MDD_3231 = ffn.calc_max_drawdown((1 + getStockReturnInfo(3231)).cumprod())

print('最大虧損 = ', MDD_3231)