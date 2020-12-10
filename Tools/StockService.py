import ffn
import matplotlib
from pandas.plotting import register_matplotlib_converters
from datetime import date

class stock():
    def __init__(self):
        super().__init__()

        matplotlib.use('TkAgg')  # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057
        register_matplotlib_converters() # 解決 pandas 要出圖的錯誤

    def getData(self, code, type , start_day):
        """取得指定股票的交易資訊

        Args:
            stock: 股票代號
            type: 股票類型(上市: tw, 上櫃: two)
            startDay: 開始交易日期
        """
        
        data = ffn.get(f"{code}.{type}:Open, {code}.{type}:High, {code}.{type}:Low, {code}.{type}:Close", start=start_day)

        # 取得時間(date)，並加入 DataFrame 之中，而且要排在第一欄，為了之後畫 K 線圖
        floteDate = data.index.to_pydatetime()
        data.insert(0, "Date", floteDate)

        # 變更欄位名稱
        data = data.rename(columns={f"{code}{type}open": 'Open', f"{code}{type}high": 'High', f"{code}{type}low": 'Low', f"{code}{type}close": 'Close'})

        return data

    def getMomentum(self, closePrice, period):
        """用【作差法】取得動量值，參考書本 p544

        Args:
            closePrice: 股票收盤價的 DataFrame
            period (integer)): 期數，滯後的天數
        """

        # 滯後 N 期的收盤價
        logClose = closePrice.shift(period)

        # 計算 N 期的動量值
        momentum = (closePrice - logClose).dropna()

        return momentum