# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:07:31 2019

@author: admin
"""

# input函数
message = input("Tell me something, and I will tell it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# int函数获取数值输入
age = input("How old are you?")
age = int(age)
if age > 18:
    print("You are an adult.")

# %运算符用于求模
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
    
# assignment7-1
car = input("Which kind of car do you want?")
print("Let me see if i can find you a " + car)
# assignment7-2
person = input("How many people have dinner together?")
person = int(person)
if person > 8 :
    print("Sorry, there's no empty table.")
# assignment7-3
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is 10 multiples.")
else:
    print(str(number) + " is not 10 multiples.")
    
# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 选择何时退出循环    
prompt = "\nTell me something, and i'll tell it back to you: "
prompt += "\nEnter 'qiut' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

# 使用标志判断整个程序是否处于活跃状态
prompt = "\nTell me something, and i'll tell it back to you: "
prompt += "\nEnter 'qiut' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
# 使用break退出整个循环, 所有循环中均可使用break循环
prompt = "\nTell me something, and i'll tell it back to you: "
prompt += "\nEnter 'qiut' to end the program."

while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(message)
        
# 使用continue退出当前循环
current_number = 0
while current_number < 10:
    current_number += 1 
    if current_number % 2 == 0:
        continue
    print(current_number)

# assignment7-5
age = input("Please enter your age: ")
age = int(age)
if age < 3:
    print("Your admission price is 0.")
elif age >= 3 and age < 12:
    print("Your admission price is $10.")
else:
    print("Your admission price is $15.")
    
# while循环处理字典与列表
unconfirmed_users = ['a', 'b', 'c']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
   
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# 使用while循环删除包含特定值的所有列表元素，remove删除列表中只出现一次的特定值
pets = ['dog', 'cat', 'goldfish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)
    
# 使用用户输入来填充字典
responses= {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you want to climb someday? ")
    # 将答案储存在字典中
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n-- Poll Results --")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    
# assignment7-8
sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("\nI made your " + sandwich_order + " sandwich.")
    finished_sandwiches.append(sandwich_order)
    
for finished_sandwich in finished_sandwiches:
    print("This sandwich had been finished: " + finished_sandwich + ".")
    
# assignment7-10
places = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    place = input("\nIf you could visit one place in the world, where would you go? ")
    places[name] = place
    polling_active = False

for name, place in places.items():
    print(name + " want to go to " + place + '.')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    