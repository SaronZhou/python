# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:21:04 2019

@author: admin
"""
import pandas as pd
import numpy as np

## pyplot ##
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16], 'ro')
# 列表[xmin,xmax,ymin,ymax]定义x轴和y轴的取值范围传给axis()函数
plt.axis([0,5,0,20])
plt.title("my plot")
plt.show()

# matploylib和numpy
import math
import numpy as np
t = np.arange(0, 2.5, 0.1)
y1 = map(math.sin, math.pi*t)
y2 = map(math.sin, math.pi*t+math.pi/2)
y3 = map(math.sin, math.pi*t-math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.show()


# 使用kwargs #
plt.plot([1,2,4,2,1,0,1,2,1,4], linewidth=2)

# subplot()函数设置分区模式与当前子图
t = np.arange(0,5,0.1)
y1 = np.sin(2*np.pi*t)
y2 = np.sin(2*np.pi*t)
plt.subplot(2,1,1)
plt.plot(t,y1,'b-.')
plt.subplot(2,1,2)
plt.plot(t,y2,'r--')

t = np.arange(0,5,0.1)
y1 = np.sin(2*np.pi*t)
y2 = np.sin(2*np.pi*t)
plt.subplot(121)
plt.plot(t,y1,'b-.')
plt.subplot(122)
plt.plot(t,y2,'r--')


## 为图标添加更多元素 ##
# 添加文本 #
# title()-添加标题、xlabel()，ylabel()—添加轴标签
# text()函数在图表任意位置添加文本
plt.axis([0,5,0,20])
plt.title("my plot", fontsize=20)
plt.xlabel('Counting', color='gray')
plt.ylabel('Square Values', color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
# 可以再图表中添加LaTeX表达式，置于两个$符号之间，在表达式之前添加字符r，表示不能对其进行转义操作
# bbox添加彩色边框
plt.text(1.1,12,r'$y=x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})
# 添加网格grid()函数
plt.grid(True)
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.plot([1,2,3,4], [0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4], [0.5,2.5,4,12], 'b*')
# legend()函数将图例和字符串类型的图例说明添加到图表中
# 图例默认添加到图形的右上角，图例的位置由loc关键字控制，取值范围为0~10
# 0：最佳位置，1：右上角，2：左上角，3：右下角，4：左下角，5：右侧，6：左侧垂直居中
# 7：右侧垂直居中，8：下方水平居中，9：上方水平居中，10：正中间
plt.legend(['First series', 'Seconf series', 'Third series'], loc=2)
# 将图表直接保存为图片
plt.savefig('my_chart.png')


# 处理日期值 #
# matplotlib.dates模块专门用于管理日起类型的数据
# MonthLocator()、DayLocator()函数分别表示月份和日期
import datetime
import matplotlib.dates as mdates
months = mdates.MonthLocator()
days = mdates.DateLocator()
timeFmt = mdates.DateFormatter('%Y-%m')
events = [datetime.date(2015,1,23), datetime.date(2015,1,28), datetime.date(2015,2,3),
          datetime.date(2015,2,21), datetime.date(2015,3,15), datetime.date(2015,3,24),
          datetime.date(2015,4,8), datetime.date(2015,4,24)]
readings = [12,22,25,20,18,15,17,14]
fig, ax = plt.subplots()
plt.plot(events, readings)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)


## 图表类型 ##
# 线形图 #
# 颜色编码 b-蓝色，g-绿色，r-红色，c-蓝绿色，m-洋红，k-黑色，y-黄色，w-白色
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x, y, 'k--', linewidth=3)
plt.plot(x, y2, 'm-.')
plt.plot(x, y3, color='#87a3cc', linestyle='--')
# xticks()、yticks()函数设定刻度标签
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],[r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
# annotate()函数适用于添加注释，第一个参数为LaTeX表达式，xy为注释的点的坐标，，xycoords为坐标系
# xytext为放置文本的坐标点，textcoords为xytext的坐标系
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}=1$', xy=[0,1], xycoords='data',
             xytext=[30,30], fontsize=16, textcoords='offset points', arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))
# gca()函数获取Axes对象，指定每条边的位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# set_ticks_position()函数设定刻度线的位置：top、bottom、both、default、none
ax.xaxis.set_ticks_position('bottom')
# spines().set_position()设定脊柱的位置，’data‘表示将脊柱放在指定的数据坐标上
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 为pandas数据结构绘制线形图
data = {'series1':[1,3,4,3,5], 'series2':[2,4,5,2,4], 'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([0,5,0,7])
plt.plot(x, df)
plt.legend(data, loc=2)


## 直方图 ##
# hist()
pop = np.random.randint(0,100,100)
n, bins, patches = plt.hist(pop, bins=20)
# n表示每个面元含有的数据量，bins代表每个面元的起始点与终止点
n
bins
patches


## 条状图 ##
# x轴表示类别，直方图x轴表示数值
index = np.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]
plt.title('Bar Chart')
# yerr=std添加标准差，常跟error_kw参数一起使用，后者接受其他可以用于显示误差线的关键字参数
# ecolor指定误差线的颜色，capsize指定误差线两头横线的宽度
plt.bar(index, values, yerr=std, error_kw={'ecolor':'0.1', 'capsize':6}, alpha=0.7, label='First')
# 第一个参数为应该放置刻度的位置列表，第二个参数为刻度标签
plt.xticks(index, ['A','B','C','D','E'])
plt.legend(loc=2)

# 水平条状图 #
# barh()函数
index = np.arange(5)
values = [5,7,3,4,6]
std = [0.8,1,0.4,0.9,1.3]
plt.title('Horizontal Bar Chart')
plt.barh(index, values, yerr=std, error_kw={'ecolor':'0.1', 'capsize':6}, alpha=0.7, label='First')
plt.yticks(index, ['A','B','C','D','E'])
plt.legend(loc=5)

# 多序列条状图 #
data = {'series1':[1,3,4,3,5], 'series2':[2,4,5,2,4], 'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='bar')
df.plot(kind='barh')

# 多序列堆积条状图 #
# 在每个bar()函数中添加bottom关键字参数，将每个序列赋给相应的bottom关键字参数
# 水平条形图将bottom关键字改为left关键字
series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([0,4,0,15])
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='b', bottom=series1)
plt.bar(index,series3,color='g', bottom=(series2+series1))
plt.xticks(index+0.2, ['Jan15','Feb15','Mar15','Apr15'])

# 使用不同的阴影填充条状图
series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([0,15,0,4])
plt.barh(index,series1,color='w', hatch='xx')
plt.barh(index,series2,color='w', hatch='///', left=series1)
plt.barh(index,series3,color='w', hatch='\\\\\\', left=(series2+series1))
plt.yticks(index, ['Jan15','Feb15','Mar15','Apr15'])


# 为pandas DataFrame绘制堆积条状图 #
# 在plot中直接绘制堆积条状图，将stacked关键字参数设置为True
data = {'series1':[1,3,4,3,5], 'series2':[2,4,5,2,4], 'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='bar', stacked=True)


# 其他条状图 #
x0 = np.arange(8)
y1 = np.array([1,3,4,6,4,3,2,1])
y2 = np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)
plt.bar(x0,y1,0.9,facecolor='r',edgecolor='w')
plt.bar(x0,-y2,0.9,facecolor='b',edgecolor='w')
plt.xticks(())
plt.grid(True)
# zip()函数它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）
for x,y in zip(x0,y1):
    plt.text(x, y+0.05, '%d' % y, ha='center', va='bottom')
for x,y in zip(x0,y2):
    plt.text(x, -y-0.05, '%d' % y, ha='center', va='top')
    

## 饼图 ##
# pie()函数
labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,35,15]
colors = ['yellow','green','red','blue']
explode = [0.3,0,0,0]
plt.title("Pie Chart")
# explode参数突出某一块，取值范围为0~1,0表示没有抽取，1表示完全脱离
# startangle参数调整饼图的旋转角度
# sutopct参数在每一块的中间位置添加文本标签来显示百分比
# shadow参数添加阴影效果
plt.pie(values, labels=labels, colors=colors, explode=explode,
        shadow=True, autopct='%1.1f%%', startangle=180)
# 绘制标准的圆形饼图
plt.axis('equal')

# 为DataFrame绘制饼图
# 每副饼图只能表示一个序列
df['series1'].plot(kind='pie', figsize=(6,6))


## 高级图表 ##
# 等值线图、等高线图 #
dx = 0.01
dy = 0.01
x = np.arange(-2.0, 2.0, dx)
y = np.arange(-2.0, 2.0, dy)
# 从坐标向量返回坐标矩阵 https://blog.csdn.net/sinat_29957455/article/details/78825945
X, Y = np.meshgrid(x, y)
def f(x, y):
    return (1 - y**5 + x**5)*np.exp(-x**2 - y**2)
# 8表示等高线的数量
# contourf()函数对等高线间的面积进行填充，而contour不会
C = plt.contour(X, Y, f(X,Y), 8, colors='black')
# camp关键字参数为选中的颜色
plt.contourf(X, Y, f(X, Y), 8, camp=plt.cm.hot)
# clabel第一个参数为contour()函数对象
plt.clabel(C, inline=1, fontsize=10)
# 对于图表中颜色的说明
plt.colorbar()


# 极区图 #
N = 8
theta = np.arange(0.,2*np.pi,2*np.pi/N)
radii = np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = np.array(['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4'])
bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)


## mplot3d ##
# axes对象转换为axes3d对象
from mpl_toolkits.mplot3d import Axes3D

# 3D曲面 #
# plot_surface()函数绘制曲面
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-2,2,0.1)
Y = np.arange(-2,2,0.1)
X, Y = np.meshgrid(X, Y)
def f(x, y):
    return (1 - y**5 + x**5)*np.exp(-x**2 - y**2)
ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1, cmap=plt.cm.hot)
# 改变视角
ax.view_init(elev=30, azim=125)


# 3D散点图 # 
# scatter()
xs = np.random.randint(30,40,100)
ys = np.random.randint(20,30,100)
zs = np.random.randint(10,20,100)
xs2 = np.random.randint(50,60,100)
ys2 = np.random.randint(30,40,100)
zs2 = np.random.randint(50,70,100)
xs3 = np.random.randint(10,30,100)
ys3 = np.random.randint(40,50,100)
zs3 = np.random.randint(40,50,100)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(xs, ys, zs)
ax.scatter(xs2, ys2, zs2)
ax.scatter(xs3, ys3, zs3)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


# 3D条状图 #
x = np.arange(8)
y = np.random.randint(0,10,8)
y2 = y + np.random.randint(0,3,8)
y3 = y2 + np.random.randint(0,3,8)
y4 = y3 + np.random.randint(0,3,8)
y5 = y4 + np.random.randint(0,3,8)
clr = ['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4']
fig = plt.figure()
ax = Axes3D(fig)
ax.bar(x,y,0,zdir='y',color=clr)
ax.bar(x,y2,10,zdir='y',color=clr)
ax.bar(x,y3,20,zdir='y',color=clr)
ax.bar(x,y4,30,zdir='y',color=clr)
ax.bar(x,y5,40,zdir='y',color=clr)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=40)


## 多面板图形 ##
# 在其他子图中显示子图 #
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# 参数列表[left, bottom, width, height]
# left、bottom为inner_axes距离画布左侧和底部的距离，width和height为宽度与高度，所有单位均是占画布的百分比
inner_ax = fig.add_axes([0.6,0.6,0.25,0.25])
x1 = np.arange(10)
y1 = np.array([1,2,7,1,5,2,4,2,3,1])
x2 = np.arange(10)
y2 = np.array([1,3,4,5,4,5,2,6,4,3])
ax.plot(x1, y1)
inner_ax.plot(x2, y2)


# 子图网络 #
# GridSpec()函数将绘图区域分成多个子区域，可以把一个或多个子区域分配给每一幅字图
# 此处的:2，达不到2，只取到1
gs = plt.GridSpec(3,3)
fig = plt.figure(figsize=(6,6))
x1 = np.array([1,3,2,5])
y1 = np.array([4,3,7,2])
x2 = np.arange(5)
y2 = np.array([3,2,4,6,4])
s1 = fig.add_subplot(gs[1, :2])
s1.plot(x1,y1,'r')
s2 = fig.add_subplot(gs[0, :2])
s2.bar(x2, y2)
s3 = fig.add_subplot(gs[2, 0])
s3.barh(x2, y2, color='g')
s4 = fig.add_subplot(gs[:2, 2])
s4.plot(x2, y2, 'k')
s5 = fig.add_subplot(gs[2, 1:])
s5.plot(x1, y1, 'b^', x2, y2, 'yo')









