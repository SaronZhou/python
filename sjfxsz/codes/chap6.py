# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:50:38 2019

@author: admin
"""

import numpy as np
import pandas as pd

### pandas数据处理 ###
# 数据准备、数据转换、数据聚合

## 数据准备 ##
# 加载、组装：合并，拼接，组合、变形（轴向旋转）、删除

# 合并 #
# merge()函数
frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'price':[12.33,11.44,33.21,13.23,33.62]})
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'color':['white','red','red','black']})
frame1
frame2
# 合并frame1与frame2
pd.merge(frame1, frame2)

# 指定基于哪一列合并，增加on选项
frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'color': ['white','red','red','black','green'],
                       'brand':['OMG','ABC','ABC','POD','POD']})
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'brand':['OMG','POD','ABC','POD']})
frame1
frame2
# frame1与frame2有两个相同列名的列，对其执行合并操作得到空DataFrame对象
pd.merge(frame1, frame2)
# 指定其合并操作标准
pd.merge(frame1, frame2, on='id')
pd.merge(frame1, frame2, on='brand')

# 使用left_on和right_on指定frame1和frame2的基准列，即以frame1中id与frame2中是sid执行合并操作
frame2.columns = ['brand','sid']
pd.merge(frame1, frame2, left_on='id', right_on='brand')

# merge()函数默认执行内连接操作，how选项可以指定连接方式
frame2.columns = ['id','brand']
pd.merge(frame1, frame2, on='id')
pd.merge(frame1, frame2, on='id', how='outer')
pd.merge(frame1, frame2, on='id', how='left')
pd.merge(frame1, frame2, on='id', how='right')

# 合并多个键
pd.merge(frame1, frame2, on=['id','brand'], how='left')

# 根据索引合并
# 将left_index与right_index选项设置为Ture，可将索引而非键作为合并的基准
pd.merge(frame1,frame2,left_index=True,right_index=True)

# DataFrame对象的join()函数更适合根据索引进行合并，可以用于合并多个索引相同或索引相同但列却不一致的DataFrame对象
frame2.columns = ['brand2','id2']
frame1.join(frame2)


## 拼接 ##
# numpy中concatenate()函数
array1 = np.arange(9).reshape((3,3))
array2 = array1 + 6
np.concatenate([array1, array2])
np.concatenate([array1, array2], axis=1)

# pandas中concat()函数实现按轴拼接的功能
ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])
# 默认按照axis=0拼接数据
pd.concat([ser1, ser2])
# 结果中无重复数据，实际上执行的是外连接操作
ser3 = pd.concat([ser1,ser2], axis=1)
pd.concat([ser1,ser3], axis=1, join='inner')

# 在用于拼接的轴上创建等级索引，keys选项
pd.concat([ser1,ser2], keys=[1,2])
# axis=1时，指定的键变为DataFrame对象的列名
pd.concat([ser1,ser2], axis=1, keys=[1,2])

frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[1,2,3],
                      columns=['A','B','C'])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[4,5,6],
                      columns=['A','B','C'])
pd.concat([frame1, frame2])
pd.concat([frame1,frame2], axis=1)


# 组合 #
# combine函数可用来组合series对象并对其数据
ser1 = pd.Series(np.random.rand(5), index=[1,2,3,4,5])
ser2 = pd.Series(np.random.rand(4), index=[2,4,5,6])
ser1
ser2
# 相同索引处使用的是ser1的值
ser1.combine_first(ser2)
# 相同索引处使用的是ser2的值
ser2.combine_first(ser1)
# 进行部分合并，索引值1,2,3,4使用的都是ser1的值
ser1[:4].combine_first(ser2[:4])

# 轴向旋转 #
# 轴向旋转有两个基础操作：入栈-旋转数据结构，将列转换为行、出栈-行转为列
# 按等级索引旋转
frame1 = pd.DataFrame(np.arange(9).reshape(3,3), index=['white','red','black'],
                     columns=['ball','pen','pencil'])
# 列转为行，得到一个series对象
ser1 = frame1.stack()
ser1.unstack()
# 出栈操作可应用于不同的层级，为unstack函数传入表示层级的编号或名称
ser1.unstack(0)
ser1.unstack(1)

# 长格式转换为宽格式 pivot()函数，可以使用键的一列或多列作为参数
# 长格式：各列都有数据项，每一列后面的数据常常会根前面的有所重复，并且常常为列表形式，有一行行数据组成
longframe = pd.DataFrame({'color':['white','white','white','red','red','red','black','black','black'],
                          'item':['ball','pen','mug','ball','pen','mug','ball','pen','mug'],
                          'value':np.random.rand(9)})
longframe
longframe.pivot('color','item')
longframe.pivot('item','color')


# 删除 #
frame1 = pd.DataFrame(np.arange(9).reshape(3,3), index=['white','black','red'],
                      columns=['ball','en','pencil'])
# 删除一列 del
del frame1['ball']
frame1
# 删除一行drop函数
frame1.drop('white')


## 数据转换 ##

# 删除重复元素 #
dframe = pd.DataFrame({'color': ['white','white','red','red','white'],
                       'value':[2,1,3,3,2]})
dframe
# duplicated()函数可用来检测重复的行，返回元素为布尔型的Series对象
# 每个元素对应一行，如果该行与其他行重复则元素为True
dframe.duplicated()
# 查找重复的行
dframe[dframe.duplicated()]
# drop_duplicates()函数返回删除重复行后的DataFrame对象
dframe.drop_duplicates()

# 映射 #
# repacle():替换元素、map()新建一列、rename()：替换索引
# 用映射替换元素
frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','rosso','verde','black','yellow'],
                      'price':[5.56,4.20,1.30,0.56,2.75]})
frame
# 用新元素替换不正确的元素，需要定义一组映射关系，旧元素作为键，新元素作为值
newcolors = {'rosso':'red', 'verde':'green'}
frame.replace(newcolors)
# 将NaN替换为正确的元素
ser = pd.Series([1,3,np.nan,4,6,np.nan,2])
ser.replace(np.nan, 0)

# 用映射添加元素 
frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow']})
price = {'ball':5.56, 'mug':4.20, 'bottle':1.3, 'scissors':3.41, 'pen':1.30, 'pencil':0.56, 'ashtray':2.75}
# map()函数可应用于series对象或是dataframe对象的一列，接收一个函数或表示映射关系的字典对象作为参数。
# item列应用映射关系，字典price作为参数
frame['price'] = frame['item'].map(price)

# 重命名轴索引
# rename()函数以表示映射关系的字典对象作为参数，替换轴的索引标签
reindex = {0:'first', 1:'second', 2:'third', 3:'fourth', 4:'fifth'}
frame.rename(reindex)
# 若要重命名各列，必须使用columns选项
recolumn = {'item':'object', 'price':'value'}
frame.rename(index=reindex, columns=recolumn)
frame.rename(index={1:'first'}, columns={'item':'object'})
# rename函数返回一个新的dataframe对象，原对象保持不变，如果要修改调用函数对象本身，可将inplace选项设置为True


## 离散化和面元划分 ##
frame.rename(columns={'item':'object'}, inplace=True)
frame
# 若实验数据范围为0~100，分为四部分即四个面元（bin）
# 定义一个数组，存储用于面元划分的各数值
bins = [0,25,50,75,100]
# 对results数组应用cut()函数，传入bins变量作为参数
results = np.random.randint(0, high=100, size=20)
cat = pd.cut(results, bins)
cat
# 显示第几个面元的index值
cat.codes
# cat()函数返回的对象为categorical类别型类型，可以看作一个字符串数组，元素为面元的名称
# levels数组为不同内部类别的名称，labels数组的元素数量跟results数组相同，labels数组的个数字表示results数组元素所属的面元
# 2.7cat.levels
# 2.7cat.labels
# 每个面元出现的次数
pd.value_counts(cat)
# 可以用字符串数组指定面元的名称，将其赋给cut函数的labels选项
bin_names = ['unlikely','less likely','likely','high likely']
pd.cut(results, bins, labels=bin_names)
# 若不指定面元的各界限，只传入一个整数作为参数，cut函数就会按照指定的数字，把数组元素取值范围划分为几部分
pd.cut(results, 5)
# 邓频分箱qcut()函数直接将样本划分为5个面元，每个面元样本数量相等，区间大小不等
quintiles = pd.qcut(results, 5)
pd.value_counts(quintiles)

# 异常值检测和过滤
# 生成3列每列1000个服从标准正态分布的随机数
randframe = pd.DataFrame(np.random.randn(1000, 3))
randframe.describe()
randframe.std()
# any函数
randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]


## 排序 ##
# np.random.permutation()函数
nframe = pd.DataFrame(np.arange(25).reshape(5,5))
new_order = np.random.permutation(5)
new_order
# 对象所有行应用take函数，将新次序传给它
nframe.take(new_order)
# 对对象的一部分进行排序操作
new_order = [3,4,2]
nframe.take(new_order)

# 随机取样
# 从[0,5)内选取三个数可重复]
sample = np.random.randint(0, len(nframe), 3)
sample
nframe.take(sample)


## 字符串处理 ##
# 内置字符串处理方法 #
# split()函数分割
text = '16 Boston Avenue, Boston'
text.split(',')
address, city = [s.strip() for s in text.split(',')]

# 字符串拼接
address + ',' + city
# 拼接数量多时，join()函数
strings = ['a','a','b','b','c','c']
';'.join(strings)

# 查找字符串
# in关键字
'Boston' in text
# index()、find()
text.index('Boston')
text.find('Boston')
# 没能查找到子串时，index()函数报错，find()函数返回-1
text.index('aaa')
text.find('aaa')

# 字符串在文本中出现的次数
text.count('o')
text.count('Boston')

# 替换子串
text.replace('Avenue', 'Street')
# 空字符替换子串，相当于删除子串
text.replace('1', '')


# 正则表达式 #
# re模块用于操作regex对象
# re模块函数：模式匹配、替换、切分
import re
text = "This is    an\t odd \n text!"
# 表示一个或多个空白字符的正则表达式为\s+，将正则表达式作为分隔符
re.split('\s+', text)

# 调用re.split()函数时，首先编译正则表达式，随后作为参数传入的文本上调用split函数
# 先用re.compile()函数编译正则表达式
regex = re.compile('\s+')
regex.split(text)

# findall()函数可匹配文本中所有符合正则表达式的子串，返回一个列表
text = "This is my address: 16 Bolton Avenue, Boston"
re.findall('A\w+', text)
re.findall('[A,a]\w+', text)

# search()函数返回第一处符合模式的子串，返回子串在字符串中的开始和结束位置
search = re.search('[A,a]\w+', text)
search.start()
search.end()
text[search.start(): search.end()]

# match()函数从字符串开头开始匹配，若第一个字符不匹配就不会再搜索字符串内部，若没能找到不会返回任何对象
re.match('[A,a]\w+', text)
match = re.match('T\w+', text)
text[match.start():match.end()]


## 数据聚合 ##
# groupby过程 #
# 分组、用函数处理、合并

# 实例 #
frame = pd.DataFrame({'color':['w','r','g','r','g'],
                      'object':['pen','pencil','pencil','ashtray','pen'],
                      'price1':[5.5,4.2,1.3,0.5,2.7],
                      'price2':[4.7,4.1,1.6,0.7,3.1]})
# 使用color列的组标签计算price1列的均值
group = frame['price1'].groupby(frame['color'])
# groups属性查看分组情况
group.groups
group.mean()
group.sum()

# 等级分组
# 使用多个键，按照等级关系分组
ggroup = frame['price1'].groupby([frame['color'], frame['object']])
ggroup.groups
ggroup.sum()
frame[['price1','price2']].groupby(frame['color']).mean()
frame.groupby(frame['color']).mean()


## 组迭代 ##
for name, group in frame.groupby('color'):
    print(name)
    print(group)

# 链式转换 #
result1 = frame['price1'].groupby(frame['color']).mean()
type(result1)
result2 = frame.groupby(frame['color']).mean()
type(result2)

# 分组操作的灵活性
frame['price1'].groupby(frame['color']).mean()
frame.groupby(frame['color'])['price'].mean()
(frame.groupby(frame['color']).mean())['price1']

# 列名添加前缀 
means = frame.groupby(frame['color']).mean().add_prefix('mean_')
means


# 分组函数
group = frame.groupby('color')
group['price1'].quantile(0.6)
# 自定义聚合函数，将其作为参数传给agg()函数
def range(series):
    return series.max() - series.min()
group['price1'].agg(range)
group.agg(range)
# 使用多个聚合函数
group['price1'].agg(['mean', 'std', range])


## 高级数据聚合 ##
# transform()函数、apply()函数
frame = pd.DataFrame({'color':['w','r','g','r','g'],
                      'price1':[5.5,4.2,1.3,0.5,2.7],
                      'price2':[4.7,4.1,1.6,0.7,3.1]})
sums = frame.groupby('color').sum().add_prefix('tot_')
pd.merge(frame, sums, left_on='color', right_index=True)
# transform()函数的参数必须生成一个标量聚合
frame.groupby('color').transform(np.sum).add_prefix('tot_')

frame = pd.DataFrame({'color':['w','r','g','r','g'],
                      'status':['u','u','d','d','d'],
                      'price1':[5.5,4.2,1.3,0.5,2.7],
                      'price2':[4.7,4.1,1.6,0.7,3.1]})
frame.groupby(['color','status']).apply(lambda x:x.max())
reindex = {0:'first', 1:'second', 2:'third', 3:'fourth', 4:'fifth'}
recolumn = {'item':'object', 'price':'value'}
frame.rename(index=reindex, columns=recolumn)
temp = pd.date_range('1/1/2015', periods=10, freq='H')
timeseries = pd.Series(np.random.rand(10), index=temp)

















