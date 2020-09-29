#-*- coding: utf-8 -*-

import ffn
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime
from cycler import cycler# 用于定制线条颜色

# pip mplfinance 參考: https://pypi.org/project/mplfinance/
# 使用新 module 的說明參考 https://www.mscto.com/python/558937.html
import mplfinance as mpf

'''
利用 python 繪製 K 線圖
'''

# 出圖
matplotlib.use('TkAgg')  # 解決出圖問題，參考 https://www.jianshu.com/p/3f4b89aaf057

# 設定開始日期
startDay = '2017-01-01'

# 設定股票代號
stock = 2330

# 取得股票資訊
data = ffn.get(f"{stock}.TW:Open, {stock}.TW:High, {stock}.TW:Low, {stock}.TW:Close", start=startDay)

# 取得時間(date)，並加入 DataFrame 之中，而且要排在第一欄，為了之後畫 K 線圖
floteDate = data.index.to_pydatetime()
data.insert(0, "Date", floteDate)

# 變更欄位名稱
data = data.rename(columns={f"{stock}twopen": 'Open', f"{stock}twhigh": 'High', f"{stock}twlow": 'Low', f"{stock}twclose": 'Close'})

"""繪製 K 線圖"""

# 圖表樣式參考: https://github.com/matplotlib/mplfinance/blob/master/examples/styles.ipynb
# 以下圖表設定參考: https://www.pythonf.cn/read/86064

# 设置基本参数
# type:绘制图形的类型，有candle, renko, ohlc, line等
# 此处选择candle,即K线图
# mav(moving average):均线类型,此处设置7,30,60日线
# volume:布尔类型，设置是否显示成交量，默认False
# title:设置标题
# y_label_lower:设置成交量图一栏的标题
# figratio:设置图形纵横比
# figscale:设置图形尺寸(数值越大图像质量越高)
""" 記得要用 dict 包起來，才可以用 **kwargs 的方式傳參數 """
kwargs = dict(
	type='candle',
	mav=(7, 30, 60),
	title=f"{stock} Information_{startDay}",
	ylabel_lower='Shares\nTraded Volume',
	figratio=(15, 10),
	figscale=1)

# 设置marketcolors
# up:设置K线线柱颜色，up意为收盘价大于等于开盘价
# down:与up相反，这样设置与国内K线颜色标准相符
# edge:K线线柱边缘颜色(i代表继承自up和down的颜色)，下同。详见官方文档)
# wick:灯芯(上下影线)颜色
# volume:成交量直方图的颜色
# inherit:是否继承，选填
mc = mpf.make_marketcolors(
	up='red', 
	down='green', 
	edge='i', 
	wick='i', 
	inherit=True)
	
# 设置图形风格
# gridaxis:设置网格线位置
# gridstyle:设置网格线线型
# y_on_right:设置y轴位置是否在右
s = mpf.make_mpf_style(
	gridaxis='both', 
	gridstyle='-.', 
	y_on_right=False, 
	marketcolors=mc)
	
# 设置均线颜色，配色表可见下图
# 建议设置较深的颜色且与红色、绿色形成对比
# 此处设置七条均线的颜色，也可应用默认设置
matplotlib.rcParams['axes.prop_cycle'] = cycler(
    color=['dodgerblue', 'deeppink', 
    'navy', 'teal', 'maroon', 'darkorange', 
    'indigo'])
    
# 设置线宽
matplotlib.rcParams['lines.linewidth'] = .5

# 图形绘制
# show_nontrading:是否显示非交易日，默认False
# savefig:导出图片，填写文件名及后缀
"""
*args    => 數個不指定 Key 的參數
**kwargs => 數個指定 key 的參數
"""
mpf.plot(data, 
	**kwargs, 
	style=s, 
	show_nontrading=False)

plt.show()