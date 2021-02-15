# -*- coding: UTF-8 -*-

# 歷史策略回測 - 固定時間買進賣出回測
# 參考課本第 44 個範例

from Utilities import Tools

tools = Tools()

# 這邊的策略用「開盤買收盤賣」，所以使用的是日線
# 20210215 小結論: 此方法針對2020年的台股似乎都會賠錢XD

# 股票資訊
code = '2330.TW'
period = '1mo'
interval = '1d'
data = tools.getStockDataByYahoo(code, period, interval)

totalProfit = 0
totalCount = 0
positiveCount = 0
negativeCount = 0
noProfitCont = 0

for index, row in data.iterrows():
    totalCount += 1
    openPrice = row['Open']
    closePrice = row['Close']
    todayProfit = closePrice - openPrice

    if todayProfit > 0:
        positiveCount += 1
    elif todayProfit == 0:
        noProfitCont += 1
    else:
        negativeCount += 1

    totalProfit += todayProfit

print('\n')
print(f"{code} 買在開盤價，賣在收盤價的交易策略為以下結果")
print(f"交易總次數: {totalCount}")
print(f"賺錢的次數: {positiveCount}，大約 {round((positiveCount/totalCount)*100, 2)} %")
print(f"賠錢的次數: {negativeCount}，大約 {round((negativeCount/totalCount)*100, 2)} %")
print(f"做白工次數: {noProfitCont}，大約 {round((noProfitCont/totalCount)*100, 2)} %")
print(f"    總收益: {totalProfit}")