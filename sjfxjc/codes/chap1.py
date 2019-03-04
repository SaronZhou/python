# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:44:45 2019

@author: admin
"""

from math import log, exp, sqrt
print("Output #1: {0:.4f}".format(exp(3)))
      
# 正则表达式与模式匹配
# re.compile将文本形式的模式编译为编译后的正则表达式
# re.I确保模式不区分大小写
# 原始字符串标志r确保python不处理字符串中的转义字符，若字符串中没有转义字符，r并非必须
# 使用re.search函数将列表中每个单词与正则表达式进行比较，若相匹配返回True
from math import log, exp, sqrt
import re

string  = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #0: {0:d}".format(count))
      
string  = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)</match_word>
print("Output: ")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))

# datetime模块
from math import log, exp, sqrt
import re
from datetime import date, time, datetime, timedelta

# 创建包含年月日的date对象，不含时间
# !s表示传入到print语句中的值应该格式化为字符串
today = date.today()
print("today: {0!s}".format(today))
print("{0!s}".format(today.year))
print("{0!s}".format(today.month))
print("{0!s}".format(today.day))
# 创建的对象包含时间元素
current_time = datetime.today()
print("{0!s}".format(current_time))

# 使用timedelta计算一个新日期
# timedelta将括号中的时间差以天、秒和毫秒的形式存储
one_day = timedelta(days=-1)
yesterday = today + one_day
print("yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("{0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# 相减的结果是个timedelta对象，将所得的差以天、小时、分钟和秒显示
date_diff = today - yesterday
print("{0!s}".format(date_diff))
print("{0!s}".format(str(date_diff).split()[0]))

# 使用strtime根据一个date对象创建具有特定格式的字符串
print("{0!s}".format(today.strftime('%m/%d/%Y')))
print("{0!s}".format(today.strftime('%b %d, %Y')))
print("{0!s}".format(today.strftime('%Y-%m-%d')))
print("{0!s}".format(today.strftime('%B %d, %Y')))

# 根据一个表示日期的字符串
# 创建一个带有特殊格式的datetime对象
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# 基于4个带有特殊格式的datetime对象，创建2个datetime对象和2个date对象
# time.strptime(date_string, format)
print("{!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("{!s}".format(datetime.strptime(date2, '%b %d, %Y')))
print("{!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("{!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))


# sorted排序函数：对一个列表集合按照列表中某个位置的元素进行排序
# 关键字函数用于设置列表排序的关键字，此处关键字函数为一个lambda函数
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key = lambda index_value: index_value[3])
print("{}".format(my_lists_sorted_by_index_3))

# operator标准模块，可以使用多个关键字对列表、元组和字典进行排序
from operator import itemgetter
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

# 使用itemgetter对一个列表集合按照两个索引位置排序
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678],
            [578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("{}".format(my_lists_sorted_by_index_3_and_0))


# 元祖解包
my_tuple = ('x', 'y', 'z')
print("{}".format(my_tuple[0]))

# 使用赋值操作符左侧的变量对元组进行解包
one, two, three = my_tuple
print("{0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("{} {}".format(var1, var2))
var1, var2 = var2, var1
print("{} {}".format(var1, var2))


# 字典中的get函数：按照键值取得相应的字典值，若不存在则返回None；若函数存在第二个参数，第二个参数为不存在键值时函数的返回值
a_dict = {'one':1, 'three':3, 'two':2}
a_new_dict = a_dict.copy()
print(a_new_dict)
print("{!s}".format(a_dict.get('three')))
print("{!s}".format(a_dict.get('four')))
print("{!s}".format(a_dict.get('four', 4)))

ordered_dict1 = sorted(a_new_dict.items(), key = lambda item:item[0])
print("Order by keys:{}".format(ordered_dict1))
ordered_dict2 = sorted(a_new_dict.items(), key = lambda item:item[1])
print("Order by keys:{}".format(ordered_dict2))
# reverse = T对应降序排列
ordered_dict3 = sorted(a_new_dict.items(), key = lambda x:x[1], reverse = True)
print("Order by keys:{}".format(ordered_dict3))
ordered_dict4 = sorted(a_new_dict.items(), key = lambda x:x[1], reverse = False)
print("Order by keys:{}".format(ordered_dict4))














