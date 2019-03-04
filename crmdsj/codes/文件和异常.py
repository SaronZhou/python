# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:34:02 2019

@author: admin
"""
# 从文件中读取数据
# 读取整个文件
# 函数open接受一个参数：要打开的文件的名称，函数返回一个表示文件的对象
# 关键字with在不再需要访问文件后将其关闭
# 可以使用open与close打开与关闭文件，此时若程序存在bug，导致close语句未执行，文件将不会关闭
# 方法rstrip删除右侧空格
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 可使用相对文件路径打开文件
file_path = 'C:\User...
with open(file_path):
    
# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object.readlines():
        print(line)
        
# 创建一个包含文件各行内容的列表
# 使用关键字with时时，open返回的文件对象只在with代码块内可用
# 要想在with代码块外使用，可在with代码块内将文件的各行储存在一个列表中
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
    
# 使用文件内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

# 测试圆周率中是否包含生日
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")
    

# 写入文件
# 写入空文件
# 函数open第二个实参以何种模式打开文件。读取模式——‘r'，写入模式——’w'，附加模式——‘a'，读取与写入模式——’r+'
# 若要写入的文件不存在，函数open将自动创建，以写入模式打开文件时，若文件已存在，将自动清空该文件
# 写入多行文件需添加换行符，否则不会自动换行
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.writa("I love creating new games.\n")

# assignment10-4
while True:
    message = input("Enter your name: ")
    print("(You can enter 'q' to quit."))
    if message != 'q':
        messages = "Hello, " + message.title() + "!" 
        print(messages)
        
        filename = 'programming.txt'
        with open(filename, 'w') as file_object:
            file_object.write(messages)
    else:
        break


# 异常：使用try-except处理异常
# 处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")    
    
# 使用异常避免崩溃
# else代码块
print("Give me teo numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number  = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number  = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")    
    else:
        print(answer)
    
# 处理FileNotFoundError
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)  
    
# 分析文本
# split以空格为分隔符将字符串拆成多个部分
title = "Alice in Wonderland"
title.split()

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)  
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# 
def count_words(filename):
    '''计算一个文件大致包括多少个单词'''
    
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except:
            msg = "Sorry, the file " + filename + " does not exist."
            print(msg)  
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
    
filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    
# except后可以接pass，在程序失败时一声不吭
 
    
# 存储数据
# 使用json模块存储数据
# json.dump()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# json.load()
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# 保存和读取用户生成的数据
import json

username = input("Enter you name: ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back,  " + username + "!")

#
import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Enter you name: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back,  " + username + "!")


# 重构：将代码划分为一系列完成具体工作的函数
import json

def greet_user():
    '''问候用户，指出其名字'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("Enter you name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back,  " + username + "!")

greet_user()

# 将上面函数重构
import json

def get_stored_username():
    '''若储存了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return none
    else:
        return username

def get_new_username():
    '''提示用户输入用户名'''
    username = input("Enter you name: ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    return username

def greet_user():
    '''问候用户，指出其名字'''
    username = get_stored_username()
    if username():
        print("Welcome back,  " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_username()






