# -*- coding: UTF-8 -*-

# 操作 Talib 技術指標計算
# 參考課本第 42 個範例

from talib.abstract import MA, BBANDS, SAR, MACD
# import 裡面的 API 包含 MA(移動平均)、BBANDS(布林通道)、SAR(拋物線轉向)、MACD(指數平滑異同移動平均線)...等

from Utilities import Tools

tools = Tools()

# 取得股票資訊
code = '2330.TW'
period = '1mo'
interval = '1d'
data = tools.getStockDataByYahoo(code, period, interval)

# 取得轉換後的資料格式(for Talib)
talibData = tools.transformToTalib(data)

# ========
# MA 的計算
# 使用 Talib 的 MA Module
# MA(data, timeperiod = 30)
# ========
MACycle = 5
MAValue = MA(talibData, timeperiod = MACycle)
print('\n')
print(f"以下是週期為 {MACycle} 的 MA 數值:")
print(MAValue)
print('\n')
print('====================================' + '\n')

# ===========
# 布林通道的計算
# BBANDS(data, timeperiod = 5)
# 請注意: 布林通道回傳的會是多個陣列，所以需要多個變數去取得結果
# 布林通道 一般是由20日的移動平均線(20MA)，加上MA的上下各2個標準差所組成
# ===========
BBANDSCycle = 10
upper, middle, lower = BBANDS(talibData, timeperiod = BBANDSCycle)
print(f"以下是 {code} 布林通道的數值:")
print('上布林值:')
print(upper)
print('\n')
print('中布林值:')
print( middle)
print('\n')
print('下布林值:')
print(lower)
print('\n')
print('====================================' + '\n')


