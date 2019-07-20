import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.anova as anova   # 此模組可以幫助進行變異數分析
import statsmodels.api as sm

'''
---- 估計回歸模型 (一元線性回歸)
---- 能夠將多個連續型或是離散型的變數之間的關係量化，進而找到事物之間的線性相關關係或是進行預測
---- Step 1 : 整理需要使用的數據
---- Step 2 : 建立一元線性回歸模型
---- 參考 P320
'''

'''
讀取台灣加權指數與台灣50指數的數據，並將 ROI 合併在一起
'''
# 取得台灣加權股價指數
TAIEX = pd.read_csv(r'D:\Code Training\Python training\financial_excel\test\台灣加權指數2019-6.csv', encoding='utf-8')
TAIEX.index = pd.to_datetime(TAIEX['日期'],)

# 取得台灣50指數
tw50 = pd.read_csv(r'D:\Code Training\Python training\financial_excel\test\\Tw50index2019-6.csv', encoding='utf-8')
tw50.index = pd.to_datetime(tw50['日期'])

# 合併兩者的日收益率(ROI)做比較
# pd.concat()  合併 DataFrame , axis =0(直向合併)/1(橫向合併)
# pd.dropna()  將缺失值(NaN)刪除
compare_df = pd.concat([TAIEX.ROI, tw50.ROI], axis=1).astype(np.float)   # astype() 欄位型別轉換
compare_df = compare_df.dropna()
compare_df.columns = ['TAXIE', 'TW50']

# 建立一元線性回歸模型
# sm.OLS(Y, sm.add_constant(X)).fit()
# Y = 𝛼 + 𝛽X + 𝜖
model = sm.OLS(compare_df.TAXIE, sm.add_constant(compare_df.TW50)).fit()

# 查詢一元回歸模型的結果
print('查詢一元回歸模型的結果', model.summary())
print('---------------------------------')

# 列出擬合模型的參數
print('列出擬合模型的參數\n', model.params)
print('---------------------------------')

# 列出擬合模型的信賴區間
print('列出擬合模型的信賴區間\n', model.conf_int())
print('---------------------------------')

# 列出模型的擬合值
print('模型的擬合值\n', model.fittedvalues[:5])
print('---------------------------------')

'''
一元線性回歸模型結果解釋
R-squared : 可決係數，表示自變數與因變數關係密切程度，其值介於0~1之間
            R^2越大，表示模型解釋的波動部分佔總波動比例越高
---------------------------------------------------------
        coef   P>|t|
const   截距項𝛼   P
X       斜率項𝛽   P
---------------------------------------------------------
如果 P < 0.05 時，coef 才存在
'''

# 常態 Q-Q圖繪製 (Normal quantile-quantile)
# 若滿足常態性假設，圖上的點應該落在一條線上
sm.qqplot(model.resid_pearson, stats.norm, line='45')
plt.show()