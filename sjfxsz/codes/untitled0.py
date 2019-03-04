# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:44:46 2019

@author: admin
"""

# ndarry:同质元素组成的多维数组
# 数据类型由dtype的NumPy对象来指定，每个ndarry只有一种dtype类型
# 数组的维数和元祖数量由数组的型（shape）来确定，数组的型由N个正整数组成的元组来指定，元组的每个元素对应每一维的大小。
# 数组的每个元素对应每一维的大小。数组的维统称为轴（axes），轴的数量被称作为秩（rank）
# NumPy数组大小固定，创建数组时一旦指定就不会发生改变
# array函数定义ndarry
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.dtype)
# 轴的数量
print(a.ndim)
# 数组长度
print(a.size)
# 数组的型
print(a.shape)

b = np.array([[1.3, 2.4], [0.3, 4.1]])
print(b)
print(b.dtype)
print(b.ndim)
print(b.size)
print(b.shape)

# 数组中每个元素的长度有几个字节
print(b.itemsize)
# 包含元组实际元素的缓冲区
print(b.data)

# 创建数组 #
# 除了列表，array函数还可以接受嵌套元组或元组列表或元组或是列表组成的列表作为参数
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)

d = np.array(((1, 2, 3), (4, 5, 6)))
print(d)

e = np.array([(1, 2,3), (4, 5, 6)])
print(e)

# 数据类型 #
g = np.array([['a', 'b'], ['c', 'd']], dtype = '|S1')
print(g)
print(g.dtype)
print(g.dtype.name)

# 可以在array函数中使用dtype选项为ndarry对象指定dtype类型
# dtype类型complex为complex128的缩写值两个64为的浮点数表示的复数， complex64为两个32为的浮点数组成的复数
f = np.array([[1, 2, 3], [4, 5, 6]], dtype = complex)
print(f)
print(f.dtype)

# zeros函数生成有shape参数指定维度信息、元素均为0的数组
# ones函数
# 默认使用float64数据类型创建数组
h = np.zeros((3,3))
print(h)
print(h.dtype)

i = np.ones((3, 3))
print(i)
print(i.dtype)

# arange函数，含左不含右， 第三个参数指定步长（可以是浮点型）
j = np.arange(4, 10，2)
print(j)
print(j.dtype)
# arange函数创建二维数组， 使用reshape函数, 按行填充
k = np.arange(1, 13).reshape(3, 4)
print(k)

# linspace函数，第三个参数表示将范围分为几个部分
l = np.linspace(0, 10, 5)
print(l)
print(l.dtype)

# 随机数填充数组
# numpy.random模块中random函数，包含元素数量由参数指定
m = np.random.random((3, 3))
print(m)
print(m.dtype)


## 基本操作 ##
# 元素运算符 #
a = np.arange(4)
print(a)
print(a + 4)
print(a * 2)
# 这些运算符为元素级，只用于位置相同的元素之间

b = np.arange(4, 8)
print(b)
print(a + b)
print(a * b)
print(a * np.sin(b))

# 多维数组仍是元素级
A= np.arange(0, 9).reshape(3, 3)
print(A)
B = np.ones((3, 3))
print(B)
print(A * B)

# 矩阵积， 非元素级
# 第一种和第二种表示方式相同，由于矩阵乘法不满足交换律，因此A*B不等于B*A
print(dot(A, B))
print(A.dot(B))
print(dot(B, A))

# 自增自减运算符
# 修改了数组的值，没有生成新数组
a = np.arange(4)
a += 1
print(a)

# 通用函数ufunc，对数组中的各个元素逐一进行操作，生成一个新的数组
a = np.arange(1, 5)
print(np.sqrt(a))
print(np.sin(a))
print(np.log(a))

# 聚合函数，对一组值进行操作，返回一个单一值
a = np.arange(1, 5)
print(np.sum(a))
print(np.min(a))
print(np.mean(a))

## 索引机制、切片和迭代方法 ##
a = np.arange(0, 10)
print(a[6])
print(a[-1])
print(a[[1, 3, 4]])

A = np.arange(10, 19).reshape(3, 3)
# 第二行第三列
print(A[1,2])

# 切片 #
a = np.arange(10, 16)
# 第三个数字指定抽取的两个元素之间的间隔大小
print(a[1:5:2])

A = np.arange(10, 19).reshape(3, 3)
# 抽取第0行
print(A[0, :])

# 数组迭代 #
# apply_along_axis函数：接收3个参数：集合函数、对哪条轴应用迭代操作和数组
# axis=0，对列进行迭代操作，值为1对行进行操作
A = np.arange(10, 19).reshape(3, 3)
print(A)
print(np.apply_along_axis(np.mean, axis=0, arr=A))
print(np.apply_along_axis(np.mean, axis=1, arr=A))

def foo(x):
    return x/2

print(np.apply_along_axis(foo, axis=1, arr=A))


## 条件和布尔数组 ##
A = np.random.random((4, 4))
print(A < 0.5)
print(A[A < 0.5])


## 形状变换 ##
# 如果行通过改变数组的形状来改变数组对象，需把表示新形状的元组直接赋给数组的shape属性
A = np.arange(10, 22).reshape(3, 4)
A.shape=(4,3)
print(A)

# ravel函数可以把多维数组再变回一维数组
A = np.arange(10, 22).reshape(3, 4)
A = A.ravel()
print(A)

# 矩阵转置：transpose函数
A = np.arange(10, 22).reshape(3, 4)
print(A.transpose())


## 数组操作 ##
# 连接数组 #
# vstack函数执行垂直入栈操作，将第二个数组作为行添加到第一个数组
# hstack函数执行水平入栈操作，将第二个数组作为列添加到第一个数组
A = np.ones((3, 3))
B = np.zeros((3, 3))
print(np.vstack((A, B)))
print(np.hstack((A, B)))

# column_stack、row_stack函数将一维数组作为列或行压入栈结构，形成一个新的多维数组
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
c = np.array([6, 7, 8])
print(np.column_stack((a, b, c)))
print(np.row_stack((a, b, c)))

# 数组切分 #
# 水平切分hsplit函数，如将4*4数组切分成两个4*2数组，垂直切分vsplit函数
A = np.arange(16).reshape((4, 4))
[B, C] = np.hsplit(A, 2)
print(B)
print(C)
[D, E] = np.vsplit(A, 2)
print(D)
print(E)

# split函数可以把数组分为几个不对称的部分，需要传入数组作为参数，指定被切分部分的索引。axis=1为列索引，axis=0为行索引，默认为0
A = np.arange(16).reshape((4, 4))
[A1, A2, A3] = np.split(A, [1,3], axis=1)
print(A1)
print(A2)
print(A3)

# 参数数组[1,3]表示分成的3个数组为arr[:1],arr[1:3],arr[3:]
[A1, A2, A3] = np.split(A, [1,3], axis=0)
print(A1)
print(A2)
print(A3)


## 常用概念 ##
# 对象的副本或视图 #
# numpy中所有赋值运算不回位数组和数组中的任何元素创建副本
a = np.array([1, 2, 3, 4])
# 将数组a赋给数组b，实际上不是为a创建副本，b只不过是数组a的另外一种方式
b = a
a[2] = 0
print(b)

# 即使是切片操作得到的结果实际上仍指向相同的随想
c = a[0:2]
a[0] = 0
print(c)

# 如果想生成一份完整的副本从而得到一个不同的数组，使用copy函数
a = np.array([1, 2, 3, 4])
d = a.copy()
a[0] = 0
print(d)

# 向量化 #

# 广播机制 #
# 两个数组的每一维等长或其中一个数组为一维
A = np.arange(16).reshape(4, 4)
b = np.arange(4)
print(A)
print(b)
print(A + b)

m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
print(m)
print(n)
print(m + n)


## 结构化数组 ##
# 结构化数组包含的是结构或记录而不是独立的元素
structured = np.array([(1, 'first', 0.5, 1+2j), (2, 'second', 1.3, 2-2j),
                       (3, 'third', 0.8, 1+3j)], dtype=('i2, a6, f4, c8'))
print(structured)
print(structured.dtype)
print(structured[1])
print(structured['f1'])

# 创建数组时，可以指定个字段的名称
structured = np.array([(1, 'first', 0.5, 1+2j), (2, 'second', 1.3, 2-2j),
                       (3, 'third', 0.8, 1+3j)], dtype=[('id', 'i2'), ('position','a6'), ('value','f4'), ('complex','c8')])
structured.dtype.names = ('id', 'order', 'value', 'complex')
print(structured)
print(structured.dtype)
print(structured['order'])


# 数组数据文件的读写 #
# 二进制文件的读写 # 
# save()方法以二进制格式保存数据，load()方法从二进制位文件中读取数据
data = np.arange(16).reshape(4, 4)
# 文件名中的.npy扩展名系统会自动添加
np.save('saved_data', data)

# 必须添加扩展名
loaded_data = np.load('saved_data.npy')
print(loaded_data)

# 读取文件中的列表形式数据 #
# genfromtxt()函数可以从文本文件中读取数据并将其插入数组中。通常有三个参数：文件名、用于分割值的字符和是否含有列标题
# 内容为空的值填充为nan
data = np.genfromtxt('data.csv', delimiter=',', names=True)









