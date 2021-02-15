# 共用的小工具

from datetime import datetime
import pandas as pd
import numpy as np
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt

# 以下兩行是解決一些 warning message 用的
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class Tools:
    def getStockDataByYahoo(self, code, period, interval):
        """透過 Yahoo Finance 的 API 取得股票資訊

        Args:
            code (string): 股票代號，例如: 2330TW
            period (string): 取得資訊的時間長度，例如: 1mo(一個月)
            interval (string): 取得的 K 線格局，例如: 1d (日線)
        """

        return yf.download(tickers=code, period=period, interval=interval)

    def getMovingAverageData(self, code, period, interval, cycle, data=None):
        """根據週期回傳移動平均的資料

        Args:
            code (string): 股票代號，例如: 2330TW
            period (string): 取得資訊的時間長度，例如: 1mo(一個月)
            interval (string): 取得的 K 線格局，例如: 1d (日線)
            cycle (integer): 移動平均的週期
            data (Dataframe | None): 如果有股票資訊可以直接帶入

        Returns:
            [Dataframe]: 回傳移動平均的 Dataframe
        """

        if  data is None:
            data = self.getStockDataByYahoo(code, period, interval)

        # 設定相關變數
        ClosePrice = []
        Time = []
        MAArray = []
        MAValue = 0
        count = 1

        for index, row in data.iterrows():
            ClosePrice += [row.Close]
            if (count < cycle):
                count += 1
                continue
            
            segmentTotal = sum(ClosePrice[(count - cycle) : count])
            MAValue = segmentTotal / cycle

            MAArray += [MAValue]
            Time += [index]

            count += 1

        MA = pd.DataFrame({'MA': MAArray}, index=Time)

        return MA

    def transformToTalib(self, data):
        """將資料轉換成 Talib 需要的格式 (資料來源需要是從 yahoo finance 取得的資料)

        Args:
            data (Dataframe): 透過 yahoo finance 拿到的股票資料

        Returns:
            [directory]: 轉換過後的格式
        """
        directory = {}

        # 把時間加入 dict
        timestampArray = data.index.values.astype(np.int64) // 10 ** 9
        time = np.array([datetime.fromtimestamp(timestamp) for timestamp in timestampArray])
        directory['time'] = time

        for column in data.columns:
            array = np.array(data[column].values)
            directory[column.lower()] = (array)

        return directory