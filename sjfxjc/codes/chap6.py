# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:08:24 2019

@author: admin
"""

### 图与图表 ###
# matplotlib、pandas、ggplot、seaborn

## matplotlib ##
# matplotlib包括条形图、箱线图、折线图、散点图和直方图
# 包括扩展工具箱：basemap、cartopy，用于制作地图，以及mplot3d用于3D绘图

# 条形图 #
# 常见条形图包括垂直图、水平图、堆积图和分组图
# 垂直条形图
import matplotlib.pyplot as plt

plt.style.use('ggplot')
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]
# 创建一个基础图
fig = plt.figure()
# 在基础图中添加一个或多个子图，第一个参数为行数，第二个参数为列数，第三个参数为索引值即第几个子图
ax1 = fig.add_subplot(1, 1, 1)
# customer_index设置条形左侧在x轴上的坐标，sale_amounts设置条形的高度，align='center'设置条形与标签中间对齐
# align另一个参数为edge
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
# 设置刻度线位置，使图形的上部和右侧不显示刻度线
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
# 将刻度线标签由客户索引值更改为实际的客户名称，rotation=0表示刻度线(ABC...)是水平的，而非倾斜一个角度，fontsize='small'设置字体为小字体
plt.xticks(customers_index, customers, rotation=0, fontsize='small')
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
# dpi=400设置图形分辨率，bbox_inches表示在保存图形时将四周的空白部分去掉
plt.savefig('mat_bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()


# 直方图 #
# 直方图用表示数值分布，常用的直方图包括频率分布、频率密度分布、概率分布和概率密度分布
# 频率分布图
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
mu1, mu2, sigma = 100, 130, 15
# 生成标准正态分布随机数，平均值分别为100,130，标准差为15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# bins=50表示每个变量的值分为50份，normed=False表示直方图显示的是频率分布而非概率密度
# alpha=0.5表示透明度
n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histgrams', fontsize=14, fontweight='bold')
ax1.set_title('Teo Frequency Distributions')
plt.savefig('mat_histgram.png', dpi=400, bbox_inches='tight')
plt.show()


# 折线图 #
from numpy.random import randn
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Grenn Dash Dot')
ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
# loc='best'表示将图例放在最合适的位置
plt.legend(loc='best')
plt.savefig('mat_line_plot.png', pdi=400, bbox_inches='tight')
plt.show()


# 散点图——相关性 #
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# 给定区间内返回均匀间隔的值，左闭右开区间
x = np.arange(start=1., stop=15., step=1.)
y_linear = x + 5. * np.random.randn(14)
y_quadratic = x**2 + 10. * np.random.randn(14)

# polyfit拟合多项式，deg为拟合多项式次数，返回对象为多项式系数组成的向量
# poly1d将多项式系数转为多项式
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# 绘制lines and/or markers.
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', \
			x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Scatter Plots with Best Fit Lines')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim((min(x)-1., max(x)+1.))
plt.ylim((min(y_quadratic)-10., max(y_quadratic)+10.))

plt.savefig('scatter_plot.png', dpi=400, bbox_inches='tight')
plt.show()


# 箱线图 #
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

N = 500
# 服从均值为loc，标准差为scale的正态分布
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
# 服从均值为mean，标准差为sigma的对数正态分布
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
# 闭区间【low，high】内的随机数
index_value = np.random.random_integers(low=0, high=N-1, size=N)
normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]
gif = plt.figure()
ax1 = gif.add_subplot(1, 1, 1)
box_labels = ['normal','normal_sample','lognormal','lognormal_sample']
# 参数notch若为True产生一个缺口的盒子图，否则生成矩形箱图
# 参数sym表示离群点形状为圆点而非默认的加号
# 参数vert为True，箱线图为竖向，否则为横向
# 参数whis设定直线从第一四分位数和第三四分位数延伸出的范围
ax1.boxplot(box_plot_data, notch=True, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Box Plots: Resampling of Two Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Value')
plt.savefig('mat_box_plot.png', dpi=400, bbox_inches='tight')
plt.show()



### pandas ###
# pandas提供可以作用与序列和数据框的函数plot，plot函数默认创建折线图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig, axes = plt.subplots(nrows=1, ncols=2)
# ravel函数将两个子图分别赋给ax1和ax2，避免使用axes[0,0]、ax[0,1]引用子图
ax1, ax2 = axes.ravel()


data_frame = pd.DataFrame(np.random.rand(5, 3), index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
                         columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metrics'))
data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')

colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
ax2.set_xlabel('Metric')
ax2.set_ylabel('Value')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.savefig('pandas_plot.png', dpi=400, bbox_inches='tight')
plt.show()


### ggplot ###
# 几何对象、图形属性、标度、统计变换、坐标系、子窗口、可视化主题
from ggplot import *

print(mtcars.head())
plt1 = ggplot(aes(x='mpg'), data=mtcars) + \
        geom_histgram(fill='darkblue', binwidth=2) +\
        xlim=(10, 35) + ylim=(0, 10) +\
        xlab('MPG') + ylab('Frequency') +\
        ggtitle('Histgram of MPG') + theme_matplotlib()

print(plt1)

print(meat.head())
plt2 = ggplot(aes(x='date', y='beef'), data=meet) +\
        geom_line(color='purple', size=1.5, alpha=0.75) +\
        stat_smooth(color='blue', size=2., span=0.15) +\
        xlab('Year') + ylab("Head of Cattle Slaughtered") +\
        ggtitle("Beef Consumption Over Time") + theme_seaborn()
print(plt2)

print(diamonds.head())
plt3 = ggplot(diamonds, aes(x='carat', y='price', color='cut')) +\
        geom_point(alpha=0.5) + scale_color_gradient(low='#05D9F6', high='#5011D1') +\
        xlim(0, 6) + ylim(0, 20000) + xlab('Carat') + ylab('Price') +\
        ggtitle("Diamond Price by Carat and Cut") + theme_gray()
print(plt3)
ggsave(plt3, 'ggplot_plots.png')


### seaborn ###
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
# seaborn支持matplot中color code来给图像添加颜色，任意matplot的color code可以与seaborn的调色盘相对应
sns.set(color_codes=True)

# 直方图
x = np.random.normal(size=100)
# distplot灵活绘制单变量观测分布, kde为核密度分布情况， rug为数据分布情况
sns.distplot(x, bins=20, kde=False, rug=True, label='Histogram w/o Density')
#sns.axlabel('Value', 'Frequency')
plt.title("Histogram of a Random Sample from a Normal Distribution")
plt.legend()

# 带有回归直线的散点图与单变量直方图
mean, cov = [5, 10], [(1, .5), (.5, 1)]
# 多元正态分布随机数
data = np.random.multivariate_normal(mean, cov, 200)
data_frame = pd.DataFrame(data, columns=['x', 'y'])
# jointplot是画两个变量或者单变量的图像，是对JointGrid类的实现
# x,y为DataFrame中的列名或者是两组数据，data指向dataframe ,kind是你想要画图的类型
sns.jointplot(x='x', y='y', data=data_frame, kind='reg').set_axis_labels('x', 'y')
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")

# 成对变量之间的散点图与单变量直方图
# 加载数据集
iris = sns.load_dataset('iris')
# 绘制数据集中的成对关系，N*N张子图，对角线为直方图，其余为散点图
# pairplot 函数可以创建一个统计图矩阵。主对角线上的图以直方图或密度图的
# 形式显示了每个变量的单变量分布，对角线之外的图以散点图的形式显示了每两个变量之
# 间的双变量分布，散点图中可以有回归直线，也可以没有。
sns.pairplot(iris)

# 按照某几个变量生成的箱线图
tips = sns.load_dataset('tips')
# 第三维度为smoker，分类变量为day，决定网格的分面
# 参数aspect为每个面的宽度
sns.factorplot(x='time', y='total_bill', hue='smoker', col='day', data=tips, kind='box', size=4, aspect=.5)

# 带有bootstrap置信区间的logistic回归模型
tips['big_tip'] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x='total_bill', y='big_tip', data=tips, logistic=True, y_jitter=.03).set_axis_labels('Total Bill', 'Big Tip')
plt.title('Logistic Regression of Big Tip vs. Total Bill')
plt.show()
savefig('seaborn_plots.png')