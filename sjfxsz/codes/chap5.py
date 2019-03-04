# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:25:13 2019

@author: admin
"""
import numpy as np
import pandas as pd

### pandas：数据读写 ###

## I/O API工具 ##
# 分为完全堆成的两大类：读取函数和写入函数

## CSV和文本文件 ##
# read_csv, read_table, to_csv

## 读取CSV或文本文件中的数据 ##
csvframe = pd.read_csv('data.csv')
# 读取CSV文件可以使用read_table函数，但必须指定分隔符为逗号
csvframe = pd.read_table('data.csv', sep=',')

# 没有表头时，使用header选项设定为None，pandas会为其添加表头
pd.read_csv('data.csv', header=None)
# 可以使用names选项指定表头 
pd.read_csv('data.csv', names=['white','red','blue','green','animal'])

# 文件中有两列作为等级索引
pd.read_csv('data.csv', index_col=['color','status'])


## 用RegExp解析TXT文件 ##
# 要解析的数据文件不是逗号或分号分隔，可以使用sep选项指定正则表达式，在read_table()函数内使用
# .换行符以外的单个字符、\d数字、\D非数字字符、\s空白字符、\S非空白字符、\n换行符、\t制表符、\uxxxx用十六进制数字xxxx表示的Unicode字符
pd.read_table('data.txt', sep='\s*')
pd.read_table('data.txt', seq='\D*', header=None)

# 解析数据时需要把空行排除在外，使用skiprows选项可以排除多余的行
# 排除前五行skiprows = 5，排除第五行skiprows = [5]
pd.read_table('data.txt',sep=',', skiprows[0,1,3,6])


## 从txt文件读取部分数据 ##
# 排除第三行不读取，nrows表示ongoing起始行往后读取多少行
pd.read_csv('data.csv', skiprows=[2], nrows=3, header=None)

# 对于一列数字，每三行执行一次求和操作
out = pd.Series()
i = 0
pieces = pd.read_csv('data.csv', chunksize=3)
for piece in pieces:
    out.set_value(i, piece['white'].sum())
    i += 1
print(out)


# 向CSV文件写入数据 #
# 将DataFrame对象写入文件时，索引和列名将一起写入
frame = pd.DataFrame(np.arange(16).reshape(4,4), index=['blue','red','yellow','white'], columns=['ball','pencil','pen','paper'])
frame.to_csv('data.csv')
# 将index和header选项设置为False可避免写入索引和列名
frame.to_csv('data.csv', index=False, header=False)

# 数据结构中的NaN写入文件后显示为空字段
frame1 = pd.DataFrame([[1,1,1,1],[2,2,2,2],[np.nan,3,3,3],[4,4,4,4]], index=['blue','red','yellow','white'], columns=['ball','pencil','pen','paper'])
frame1
frame1.to_csv('data.csv')
# 使用na_rep选项将空字段提汗味需要的值
frame1.to_csv('data.csv', na_rep='NaN')


## 读写HTML文件 ##
# read_html()   to_html()

# 写入数据到HTML文件 #
frame = pd.DataFrame(np.arange(16).reshape(4,4))
print(frame.to_html())

# 将DataFrame对象写入HTML页面
frame = pd.DataFrame(np.random.random((4,4)), index=['white','red','blue','black'],
                     columns=['up','down','left','right'])
frame
# 创建一个包含HTML页面代码的字符串
s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)
# 将页面所有内容储存在变量HTML中
html_file = open('myframe.html', 'w')
html_file.write(html)
html_file.close()

# 从HTML文件读取数据
# 即使只有一个表格，read_html函数也会返回一个DataFrame列表
web_frames = pd.read_html('myframe.html')
web_frames[0]

# read_html函数最常用的模式事宜网址作为参数，直接解析并抽取网页中的表格
ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
ranking[0]


## 从XML（可扩展标记语言）读取数据 ##

## 读写Excel文件 ##
# read_excel()  to_excel()
pd.read_excel('data.xls')
# 默认返回第一个工作表中的数据，第二个蚕食指定工作表的名称或是序号
pd.read_excel('data.xls', 'Sheet2')

frame.to_excel('data.xls')


## JSON（javascript对象标记 ##
# read_json()   to_json()
frame = pd.DataFrame(np.random.random((4,4)), index=['white','red','blue','black'],
                     columns=['up','down','left','right'])
frame.to_json('frame.json')

pd.read_json('frame.json')

# json文件中的数据不是列表形式时，需要将字典结构的文件转换为列表形式，称为规范化
from pandas.io.json import json_normalize
file = open('books.json', 'r')
text = file.read()
text = json.loads(text)
json_normalize(text, 'books')
json_normalize(text, 'books',['writer','nationality'])


## HDF5格式 ##

## pikle——python对象序列化 ##












