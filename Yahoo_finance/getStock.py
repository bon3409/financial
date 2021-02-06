# 可以使用 yahoo finance 取得不同週期的 K 線

import fix_yahoo_finance as yf

# Get the data
# 參考: https://pypi.org/project/yfinance/
data = data = yf.download(
        # tickers list or string as well
        tickers = "8086.TWO 2330.TW",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        # 台股上櫃(TWO)最小範圍至少要 2d 以上的範圍
        period = "2d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'column',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

# Print all data
print('全部資料')
print(data.tail())
print('\n')

# print specific column
print('指定欄位資料')
print(data['Close'].tail())
print('\n')

# # print specific column and stock info
print('指定欄位的股票資訊')
print(data['Close']['8086.TWO'].tail())
print('\n')

