import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats  # 統計函數的套件

'''
---- 台灣加權股價指數(TAIEX) 與台灣50指數(tw50)的相關分析
---- 參考 P275
'''

# 取得台灣加權股價指數
TAIEX = pd.read_csv('Statistics\excel\台灣加權指數2019-6.csv', encoding='utf-8')
TAIEX.index = pd.to_datetime(TAIEX['日期'],)

# 取得台灣50指數
tw50 = pd.read_csv('Statistics\excel\Tw50index2019-6.csv', encoding='utf-8')
tw50.index = pd.to_datetime(tw50['日期'])


# 合併兩者的日收益率(ROI)做比較
# pd.concat()  合併 DataFrame , axis =0(直向合併)/1(橫向合併)
# pd.dropna()  將缺失值(NaN)刪除
compare_df = pd.concat([TAIEX.ROI, tw50.ROI], axis=1).astype(np.float)   # astype() 欄位型別轉換
compare_df = compare_df.dropna()
compare_df.columns = ['TAXIE', 'TW50']

# 計算加權指數與台灣50指數的收益率相關係數
relaction_coefficient = compare_df.TAXIE.corr(compare_df.TW50)
print('加權指數與台灣50指數的收益率相關係數 = ', relaction_coefficient)

# 繪製台灣加權股價(TAIEX) 與台灣50指數(tw50) 的日收益率(ROI) 散點圖(scatter)
# plt.scatter(compare_df['TAXIE'], compare_df['TW50'])
''' 
如果散點圖呈現 "左下→右上＂的方向擴散，表示此兩個數據呈現 "正相關性" !!!!!!!!!!!
'''
plt.scatter(compare_df.TAXIE, compare_df.TW50)
plt.title('2019/6 加權指與台灣50指數收益率散點圖\n相關係數 = {}'.format(relaction_coefficient))
plt.xlabel('加權指數收益率')
plt.ylabel('台灣50指數收益率')
plt.show()