import pandas as pd
import statsmodels.stats.anova as anova   # 此模組可以幫助進行變異數分析
from statsmodels.formula.api import ols   # Create a Model from a formula and dataframe.

'''
---- 單因素變異數分析
---- 分析 : 行業類別是否會影像收益率
---- Step 1 : 建立一個線性回歸模型
---- Step 2 : 將模型作為參數傳回函數中 
---- 參考 P307
'''

# 取得各類別收益率報表
year_return = pd.read_csv(r'D:\Code Training\Python training\financial_excel\test\類股變異數分析.csv', encoding='utf-8')
print(year_return)
print('-----------------')

# 進行變異數分析
# 建立線性回歸分析模型，參考 P.320
# ols(formula, data)
# formula : str or generic Formula object (The formula specifying the model)
# data : array-like (data must define __getitem__ with the keys in the formula terms args and kwargs are passed on to the model instantiation. E.g., a numpy structured or rec array, a dictionary, or a pandas DataFrame.)
# ols('反應變數 ~ C(因子變數1+因子變數2+...)', 數據資料)
model = ols(formula='Return ~ Industry', data=year_return.dropna()).fit()

table1 = anova.anova_lm(model)
print('變異數分析的結果，我們要觀察 PR(>F) 這個項目')
print(table1)
print('-----------------')
print('如果 PR < 0.05 ，則代表因子變數對反應變數 [有影響]')
print('如果 PR > 0.05 ，則代表因子變數對反應變數 [無影響]')