import pandas as pd
import ffn
import matplotlib
import matplotlib.pyplot as plt

'''
---- 利用 ffn 模組出圖
'''

def getStockInfo(stock_name, start_date=None):
    ''' get stock info from yahoo finance'''
    return ffn.get(stock_name, start=start_date)

def getStockReturnsInfo(stock_name, start_date=None):
    '''取得股票收益率'''
    return ffn.to_returns(ffn.get(stock_name, start=start_date))

def getAnnualize(stock_name, start_date=None):
    '''取得股票累積收益率'''
    return (1 + ffn.to_returns(ffn.get(stock_name, start=start_date))).cumprod() - 1