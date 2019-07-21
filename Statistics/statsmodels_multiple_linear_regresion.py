import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.anova as anova   # 此模組可以幫助進行變異數分析
import statsmodels.api as sm

'''
---- 估計回歸模型 (多元線性回歸)
---- 能夠將多個連續型或是離散型的變數之間的關係量化，進而找到事物之間的線性相關關係或是進行預測
---- Step 1 : 整理需要使用的數據
---- Step 2 : 建立一元線性回歸模型
---- 參考 P320
'''

# 讀取數據
table = pd.read_csv(r'D:\Code Training\Python training\financial_excel\test\Taiwan_GDP_table.csv')
'''
---- rgdpe : 實質 GDP
---- pl_c  : 居民消費價格水準 (Price level of hoursehold consumption)
---- pl_i  : 資本形成品價格水準 (Price level of capital formation)
---- pl_g  : 政府採購價格水準 (Price level of government consumption)
---- pl_x  : 出口品的價格水準 (Price level of exports)
---- pl_m  : 進口品的價格水準 (Price level of imports)
---- pl_n  : 資本存量的價格水準 (Price level of capital stock)
---- pl_k  : 資本服務的價格水準 (Price level of capital services)
'''

# 建立模型
model = sm.OLS(np.log10(table.rgdpe), sm.add_constant(table.iloc[:,-7:])).fit()
print(model.summary())   # 查詢模型結果

''' 結果:
                            OLS Regression Results
==============================================================================
Dep. Variable:                  rgdpe   R-squared:                       0.958
Model:                            OLS   Adj. R-squared:                  0.952
Method:                 Least Squares   F-statistic:                     177.3
Date:                Sun, 21 Jul 2019   Prob (F-statistic):           2.28e-35
Time:                        15:36:13   Log-Likelihood:                -7.0540
No. Observations:                  63   AIC:                             30.11
Df Residuals:                      55   BIC:                             47.25
Df Model:                           7
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         11.1846      0.350     31.964      0.000      10.483      11.886
pl_c           7.0379      2.828      2.489      0.016       1.371      12.705
pl_i          -3.4398      2.443     -1.408      0.165      -8.336       1.456
pl_g          -1.8225      2.264     -0.805      0.424      -6.361       2.716
pl_x          -2.3786      3.480     -0.683      0.497      -9.353       4.596
pl_m           6.2104      2.827      2.197      0.032       0.544      11.877
pl_n          -0.1972      1.915     -0.103      0.918      -4.035       3.641
pl_k          -1.7758      0.386     -4.606      0.000      -2.548      -1.003
==============================================================================
Omnibus:                        0.496   Durbin-Watson:                   0.247
Prob(Omnibus):                  0.780   Jarque-Bera (JB):                0.258
Skew:                          -0.156   Prob(JB):                        0.879
Kurtosis:                       3.029   Cond. No.                         193.
==============================================================================
上面的結果是不考慮因素之間的共線性，所以需要將有共線性的因素排除掉
'''

# 檢視各因素之間的相關性
print(table.iloc[:,-7:].corr())
'''
以下為因素之間的相關性
==========================================================================
          pl_c      pl_i      pl_g      pl_x      pl_m      pl_n      pl_k
pl_c  1.000000  0.988777  0.977863  0.964155  0.975582  0.977696 -0.392631
pl_i  0.988777  1.000000  0.990694  0.980319  0.980469  0.952671 -0.474184
pl_g  0.977863  0.990694  1.000000  0.986077  0.978997  0.927741 -0.502593
pl_x  0.964155  0.980319  0.986077  1.000000  0.994057  0.901232 -0.557739
pl_m  0.975582  0.980469  0.978997  0.994057  1.000000  0.926425 -0.508650
pl_n  0.977696  0.952671  0.927741  0.901232  0.926425  1.000000 -0.266450
pl_k -0.392631 -0.474184 -0.502593 -0.557739 -0.508650 -0.266450  1.000000
==========================================================================
結論 : 發現多數參數皆擁有共線性，所以此多元線性回歸的結果不能真實反映真實情況
'''