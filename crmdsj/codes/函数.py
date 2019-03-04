# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 09:57:29 2019

@author: admin
"""

# 定义函数
def greet_user():
    '''显示简单的问候语'''
    print("Hello!")
    
greet_user()

# 向函数传递信息
def greet_user(username):
    print("Hello, " + username + " !")
    
greet_user('Saron')

# assignment8-1
def display_message():
    print("I'm learning definition this chapter.")

display_message()
# assignment8-2
def favoriate_book(title):
    print("\nOne of my favoriate book is " + title.title() + ".")

favoriate_book("alice in wonderland")

# 传递实参
# 位置实参
def describe_pet(animal_type, pet_name):
    '''显示动物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describe_pet('hasmer', 'harry')

# 关键字实参，无需考虑参数位置
def describe_pet(animal_type, pet_name):
    '''显示动物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describe_pet(pet_name = 'harry', animal_type = 'hasmer')

# 默认值，定义函数时可以给形参指定默认值，调用函数没有给出相应的实参时，函数将使用默认值。
def describe_pet(pet_name, animal_type = 'dog'):
    '''显示动物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describe_pet(pet_name = 'harry')
# 此处调换了两个形参的位置，因为animal_type指定了默认值，因此调用函数只有一个实参，python依旧将其认为位置实参
def describe_pet(animal_type = 'dog', pet_name):
    '''显示动物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describe_pet('harry')
# 这种定义方式将会报错：SyntaxError: non-default argument follows default argument

# assignment8-3
def make_shirt(size, words):
    print("\nThis T_shirt's size is " + str(size) + " and words: " + words + '.')

make_shirt('M', 'I have a dream.')
# assignment8-5
def describe_city(city, country):
    print("\n" + city + " is in " + country + ".")

describe_city('Beijing', 'China')

# 返回返回值——使用return语句返回返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

user = get_formatted_name('John', 'Cena')
print(user)

# 使实参变为可选
def  get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

user_0 = get_formatted_name('John', 'Cena')
print(user_0)
user_1 = get_formatted_name('Klay', 'Steven', 'Jordan')
print(user_1)

# 返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = ''):
    # age为可选的参数
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 20)
print(musician)

# 结合while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit.)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
       break
   
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
# assignment8-6
def city_country(city, country):
    print("\n" + city.title() + ", " + country.title())
    
city_country('santiago', 'cheli' )
city_country('beijing', 'china')
city_country('washington', 'america')
# assignment8-7
def make_album(musician, album_name, song_number = ''):
    if song_number:
        album = {'musician': musician, 'album_name': album_name,
                 'song_number': song_number}
    else:
        album = {'musician': musician, 'album_name': album_name}
    
    return album

album = make_album('TS', '22')
print(album)
album = make_album('TS', 'Red', 20)
print(album)
# assignment8-8
def make_album(musician, album_name, song_number = ''):
    if song_number:
        album = {'musician': musician, 'album_name': album_name,
                 'song_number': song_number}
    else:
        album = {'musician': musician, 'album_name': album_name}
    
    return album

while True:
    musician = input('musician: ')
    if musician == 'q':
       break
    album_name = input('album_name: ')
    if musician == 'q':
       break
    # 输入歌曲数量时之间回车，代表歌曲数量为空
    song_number = input("song_number: ")
    if song_number == 'q':
        break
    
    album = make_album(musician, album_name, song_number)
    print(album)
    
# 向函数传递列表
def greet_user(usrnames):
    for name in usernames:
        print("\nHello, " + name + "!")

usernames = ['a', 'b', 'c']
greet_user(usernames)

# 在函数中修改列表
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        
        print("Printing model: " + current_model)
        completed_model = completed_models.append(current_model)
        
def show_completed_models(completed_models):
    '''显示打印好的模型'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_models = ['a', 'b', 'c']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表
# 若上述函数中unprinted_models需要保留原来的列表而修改后列表为空，可以使用列表副本而非列表本身
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        
        print("Printing model: " + current_model)
        completed_model = completed_models.append(current_model)
        
def show_completed_models(completed_models):
    '''显示打印好的模型'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_models = ['a', 'b', 'c']
completed_models = []

print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print(unprinted_models)

# assignment8-9
def show_magicians(magicians):
    for magician in magicians:
        print("\nHello, " + magician + ' !')
    
magicians = ['a', 'b', 'c']
show_magicians(magicians)
# assignment8-10
def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append(current_magician)
    
def show_magicians(magicians):
    for magician in magicians:
        print("\nHello, " + magician + ' !')
    
magicians = ['a', 'b', 'c']
great_magicians = []

make_great(magicians, great_magician)
show_magicians(magicians)
show_magicians(great_magician)

# 传递任意数量的实参
# 使用*创建一个名为toppings的空元组
def make_pizza(*toppings):
    '''概述要制作的披萨'''
    print("\nMakeing a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 位置实参和任意数量实参的混合使用，必须将任意数量实参放在最后
def make_pizza(size, *toppings):
    '''概述要制作的披萨'''
    print("\nMakeing a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(10, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    '''创建一个字典，其中有关于用户的一切'''
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', 
                             location = 'princeton', field = 'physics')
print(user_profile)

# assignment8-14
def make_car(producer, type, **car_info):
    profile = {}
    profile['producer'] = producer
    profile['type'] = type
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

# 将函数储存在模块中：可将函数储存在被称为模块的独立文件中，再将模块导入到主程序中
# import语句允许在当前运行的程序文件中使用模块中的代码
# 模块是扩展名为.py的文件
# 创建一个名为pizza.py的文件
import pizza
# 导入模块pizza
# module_name.dunction_name使用函数

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers')

# 导入特定的函数：from module_name import function_name1, function_name2, ...
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers')

# 使用as给函数指定别名：from module_name import function_name as fn
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers')

# 使用as给模块指定别名：import module_name as mn
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers')

# 使用*导入模块中所有函数:from module_name import *
# 使用并非自己编写的大型模块时， 最好不要使用这种方法，Python可能遇到多个名称相同的函数，进而覆盖函数
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers')

# 编写函数时，应给函数指定描述性名称，且只在其中使用小写字母与下划线
# 每个函数都应该包含简要的阐述其功能的注释，并采用文档字符串格式
# 给形参指定默认值时，等号两边不要有空格，调用关键字实参，等号两边也不要有空格
# 所有的import语句都应该放在开头，除非文件开头使用了注释来描述整个程序




















