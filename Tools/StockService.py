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