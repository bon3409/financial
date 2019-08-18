# Python 量化投資說明

## 機率密度函數 PDF (Probability Density Function)

### 用途 : 
1. 利用 stats 中 gaussian_kde() 方法可以估計機率密度
2. 利用 cumsum() 可以計算出累積分布

## 1. 二項分布 (Binomial Distribution)
二項分布即為重複 N 次的伯努力試驗
伯努力試驗中的結果只有 "成功" or "失敗" 兩種

### 用途 : 
1. 可以估計股票在未來 N 個交易日中，有 M 天會上漲的機率為多少

## 2. VaR 應用 (Value at Risk)
在一定的信賴區間下及在特定的"期間"與"機率"下，投資可能產生的最大損失

### 用途 :
1. 可以評估投資商品在金融市場裡的風險值

## 3. 變異數相關分析

### 用途 : 
可以判斷變異樹枝間的相關性，評估是否為 "正相關"

## 4. 信賴區間估計
是對產生這個樣本的母體的參數分布（Parametric Distribution）中的某一個未知參數值，以區間形式給出的估計

### 用途 :
1. 可以估算出母體樣本的範圍值，例如股票收益率的範圍等

## 5. 變異數分析
變異數分析的目的在於分析因子對反應變數有無顯著的影響

### 用途 : 
1. 可以分析單一或多因素影響股票收益的狀況，例如:產業類別...

## 6. 線性回歸分析
回歸分析可以將多個連續型或是離散型的變數之間的關係量化，進而找找到事物之間的線性相關關係，或是進行預測
1. 一元線性回歸
2. 多元線性回歸

### 用途 : 
1. 可以幫助了解變數之間的關聯性，以及更明確了解哪個變數影響最大

## 單期收益與多期收益率
評估金融商品的投資效益的狀況

### 用途 :
1. 計算年化收益率