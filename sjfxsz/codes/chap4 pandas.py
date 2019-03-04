# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:56:15 2019

@author: admin
"""
import pandas as pd
import numpy as np
### pandas ###

## pandas数据结构简介 ##
# pandas核心为两大数据结构：Series及DataFrame

# Series对象 #
# 用来表示一维数据结构
# 调用Series()构造函数
s = pd.Series([12, -4, 7, 9])
# 左侧为index是一列标签，声明series时，若不指定标签，默认使用从0开始递增的数值作为标签
print(s)
print(s.dtype)

s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
print(s)
print(s.dtype)

# 调用series对象的两个属性
print(s.values)
print(s.index)

# 选取series对象内部的元素
print(s[2])
print(s['b'])
print(s[0:2])
print(s[['a', 'b']])

# 为元素赋值
s['b'] = 1
print(s) 

# 用numpy数组或其他series对象定义新series对象
arr = np.array([1, 2, 3, 4])
s3 = pd.Series(arr)
print(s3)
s4 = pd.Series(s)
print(s4)
# 新Series对象并非是原来的副本，而是改变原有对象元素的值，新的series对象元素也会改变
arr[2] = -2
print(s3)

# 筛选元素
print(s[s > 8])

# series对象运算和数学函数
print(s / 2)
print(np.log(s3))

# series对象的组成元素
serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])
print(serd)
# unique函数包含多少不同的元素
print(serd.unique())
# value_count函数返回各个不同元素及其出现的次数
print(serd.value_counts())
# isin函数判断所属关系，返回布尔值
print(serd.isin([0, 3]))

# NAN
s2 = pd.Series([5, -3, np.NaN, 14])
print(s2)
# isnull函数和notnull函数用来识别没有对应元素的索引是非常好用
print(s2.isnull())
print(s2.notnull())
print(s2[s2.isnull()])

#series用作字典
mydict = {'red':2000, 'blue':1000, 'yellow':500, 'orange':1000}
myseries = pd.Series(mydict)
print(myseries)

# series对象之间的运算，能够通过识别标签对其不一致的数据，索引不一致的值为NaN
mydict2 = {'red':400, 'yellow':1000, 'black':700}
myseries2 = pd.Series(mydict2)
print(myseries + myseries2)


# DataFrame对象 #
# 各列的数据对象可以不同 
# 定义DataFrame对象：传递一个dict对象给DataFrame构造函数
data = {'color':['blue','green','yellow','red','white'],
        'object':['ball','pen','pencil','paper','mug'],
        'price':[1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
print(frame)
# 选择需要的列创建DataFrame对象
frame2 = pd.DataFrame(data, columns=['object','price'])
print(frame2)
# 设定索引
frame3 = pd.DataFrame(data, index=['one','two','three','four','five'])
print(frame3)

# 定义DataFrame，指定3个参数：数据矩阵、index选项、columns选项
frame4 = pd.DataFrame(np.arange(16).reshape(4,4), index=['red','bule','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
print(frame4)

# 选取元素 
# 调用columns属性得到DataFrame对象所有列的名称
print(frame4.columns)
print(frame4.index)
print(frame4.values)
print(frame4['paper'])
# 用列名作为DataF实例的属性
print(frame4.paper)
# ix属性和行的索引值得到对象中的行
print(frame4.ix[2])
print(frame4[0:2])
# 选取一个元素
print(frame4['pencil'][3])

# 赋值
# 使用name属性为index和columns这两个二级结构指定标签
frame4.index.name = 'color'
frame4.columns.name = 'item'
print(frame4)
# 为对象添加新列
frame4['new'] = 12
print(frame4)
frame4['new'] = [3.0,1.3,1.2,2.2]
print(frame4)

ser = pd.Series(np.arange(4))
print(ser)
frame4['new2'] = ser
print(frame4)
print(frame4['new2'])

# 元素的所属关系
print(frame4.isin([1,2]))
# 只包含满足条件的元素，其余均为NaN
print(frame4[frame4.isin([12,14])])

# 删除一列
del frame4['new2']
print(frame4)

# 筛选，不符合条件的元素替换为NaN
print(frame4[frame4 < 12])

# 用嵌套字典生成DataFrame对象
# 外部的键解释为列名称，内部的键解释为用作索引的标签
nestdict = {'red':{2012:22, 2013:33}, 'white':{2011:13, 2012:22, 2013:16}, 'blue':{2011:17, 2012:27, 2013:18}}
frame5 = pd.DataFrame(nestdict)
print(frame5)

# DataFrame转置，调用T属性
print(frame5.T)


# index对象 #
# 与pandas数据结构中其他元素不同的是，index对象不可改变

# index对象的方法
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
print(ser)
print(ser.idxmax())
print(ser.idxmin())

# 含有重复标签的index
serd = pd.Series(range(6), index=['white','white','blue','green','green','yellow'])
print(serd)
print(serd['white'])
# is_unique属性，是否存在重复的索引项
print(serd.index.is_unique)


## 索引对象的其他功能 ##

# 更换索引 #
ser = pd.Series([2,5,7,4], index=['one','two','three','four'])
# reindex函数可更换Series对象的索引。根据新标签序列，重新调整原Series的元素，生成一个新的Series对象
# 更换索引是，可以调整索引序列中个标签的顺序，删除或增加新标签，如增加新标签，添加NaN作为其元素
print(ser.reindex(['three','four','five','one']))

# 自动填充或差值
ser2 = pd.Series([1,5,6,3], index=[0,3,5,6])
print(ser2)
# 添加了原Series对象缺失的索引项，元素值为索引编号比它小的那一项的元素
# method：ffill/pad最后一次有效观察填补空白；backfill/bill下一个有效观察来填补空白；neares最近的有效观察填补空白
ser2.reindex(range(6), method='ffill')

data = {'object':['ball','pen','pencil','paper','mug'],
        'color':['blue','green','yellow','red','white'],
        'price':[1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
print(frame)
frame.reindex([0,1,2,3,4], method='ffill', columns=['price','color','object','new'])

#  删除 #
ser = pd.Series(np.arange(4.), index=['blue','red','yellow','white'])
print(ser)
ser.drop(['yellow', 'white'])

frame = pd.DataFrame(np.arange(16).reshape(4,4), index=['blue','red','yellow','white'], columns=['ball','pencil','pen','paper'])
# 删除行只需传入行的索引
frame.drop(['blue','white'])
# 删除列需传入参数axis=1
frame.drop(['pen','pencil'], axis=1)

# 算术和数据对齐 #
# pandas能够将两个数据结构的索引对齐 
s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1], ['white','yellow','black','blue','brown'])

s1 + s2

frame1 = pd.DataFrame(np.arange(16).reshape(4,4), index=['blue','red','yellow','white'], columns=['ball','pencil','pen','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape(4,3), index=['blue','green','white','yellow'], columns=['mug','pen','ball'])
frame1 + frame2


## 数据结构之间的运算 ##
# 算术运算方法 #
# add、sub、div、mul
frame1.add(frame2)

# DataFrame和Series对象之间的运算 #
frame = pd.DataFrame(np.arange(16).reshape(4,4), index=['blue','red','yellow','white'], columns=['ball','pencil','pen','paper'])
ser = pd.Series(np.arange(4.), index=['ball','pencil','pen','paper'])
print(frame)
print(ser)
frame - ser

ser['mug'] = 9
frame - ser


## 函数应用和映射 ##
# 操作元素的函数 #
# 通用函数np.sqrt函数能计算DataFrame对象每个元素的平方根
print(frame)
np.sqrt(frame)

# 按行或列执行操作的函数 #
f = lambda x : x.max() - x.min()
# 或者定义函数
# apply函数可以在DataFrame对象上调用刚定义的函数
# 默认对列操作，axis=1对行操作
frame.apply(f, axis=1)
frame.apply(f)
# apply函数返回DataFrame对象
def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])
frame.apply(f)


# 统计函数 #
# 默认按列求和
print(frame.sum())
print(frame.sum(axis=1))
print(frame.mean())
frame.describe()


# 排序和排位次 #
# sort_index()函数返回一个跟元独享相同但顺序不同的新对象
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
# 按照索引进行排序
ser.sort_index()
# 默认进行升序排列，修改参数ascengding进行降序排列
ser.sort_index(ascending=False)

# 默认按索引进行排列
frame.sort_index()
# 按列进行排列
frame.sort_index(axis=1)
# 对某一列进行排序
frame.sort_index(by=['pen', 'paper'])

# 排位次操作为序列的每一个元素安排一个位次（初始为1，一次加1）
ser.rank()
# method=first将数据在数据结构中的顺序（没有进行排序操作）作为位次
ser.rank(method='first')


# 相关性和协方差 #
# corr()函数与cov()函数
seq = pd.Series([3,4,3,4,5,4,3,2], ['2006','2007','2008','2009','2010','2011','2012','2013'])
print(seq)
seq2 = pd.Series([1,2,3,4,4,3,2,1], ['2006','2007','2008','2009','2010','2011','2012','2013'])
seq.corr(seq2)
seq.cov(seq2)

frame.cov()
frame.corr()

# corrwith()方法计算DataFrame对象的行或列与Series对象或其他DataFrame对象两两之间的相关性
frame.corrwith(ser)


## NaN数据 ##
# 为元素赋NaN值 #
# np.nan
ser = pd.Series([0,1,2,np.nan,9])
print(ser)
ser[2] = None
print(ser)

# 过滤NaN #
ser.dropna()
ser[ser.notnull()]
# 对DataFrame对象使用dropna()方法，只要行或列中有一个nan，会删除整行或者整列
frame2 = pd.DataFrame([[6,np.nan,6], [np.nan,np.nan,np.nan], [2,np.nan,5]], 
                      index = ['blue','green','red'], columns=['ball','mug','pen'])
frame2.dropna()
# 使用how选项避免删除整行或是整列
frame2.dropna(how='all')

# 为NaN元素填充其他值 #
# fillna()函数，参数为替换NaN的值
frame2.fillna(0)
#将不同列的NaN替换为不同的元素
frame2.fillna({'ball':1, 'mug':2, 'pen':99})


# 等级索引和分级 #
# 创建包含两层的数据结构
mser = pd.Series(np.random.rand(8), index=[['white','white','white','blue','blue','red','red','red'],
                 ['up','down','right','up','down','up','down','left']])
print(mser)
mser.index
mser['white']
mser[:, 'up']
mser['white', 'up']

# 调整数据形状，unstack函数与stack函数
# 长表转换为宽表
mser.unstack()
# 宽表转换为长表，转换时自动删去了NaN
frame2.stack()

# 为frame对象都定义等级索引，为index和columns选项都设定一个元素为数组的数组
mframe = pd.DataFrame(np.random.randn(16).reshape(4,4), index=[['white','white','red','red'], ['up','down','up','down']],
                      columns=[['pen','pen','paper','paper'], [1,2,1,2]])
print(mframe)


# 重新调整顺序和为层级排序 #
# 为层级设定名称
mframe.index.names = ['colors','status']
mframe.columns.names = ['objects','id']
print(mframe)
# swaplevel()函数以要互换位置的两个层级名称为参数
mframe.swaplevel('colors','status')
# sortlevel()函数只根据一个层级对数据排序
mframe.sortlevel('colors')


# 按层级统计数据 #
# 将层级的名称赋给level选项
mframe.sum(level = 'colors')
# 对某一层级的列进行统计，需把axis设置为1
mframe.sum(level = 'id', axis=1)




