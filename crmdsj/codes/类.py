# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:42:10 2019

@author: admin
"""

# 创建类
# __init__方法是一个特殊的方法，每当根据Dog类创建新类时，python都会自动运行它#
# 其中形参self必不可少，还必须位于其他形参前面。python调用__init__创建Dog类实例时，将自动传入实参self
# 每个与类相关联的方法调用都自动传入实参self，它是一个纸箱实例的引用
# 以self为前缀的变量可以供类中的所有方法使用，可以通过类的任何实例来访问这些变量
class Dog():
    '''创建一个小狗的类'''
    
    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age
        
    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + " rolled over.")
        
# 根据类创建实例
my_dog = Dog('willie', 6)        

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

# 创建多个实例
your_dog = Dog('lucy', 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()

# assignment9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        print("\nThis restaurant's name is: " + self.name)
        print("Cuisine type: " + self.type)
        
    def open_restaurant(self):
        print("is open")

restaurant = Restaurant("a", "b")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# assignment9-3
class User():
    def __init__(self, first_name,last_name, age):
        '''初始化描述客户的信息'''
        self.first = first_name
        self.last = last_name
        self.age = age
        
    def describe_user(self):
        '''打印客户信息摘要'''
        print("First name: " + self.first.title())
        print("Last name: " + self.last.title())
        print("Age: " + str(self.age))
        
    def greet_user(self):
        '''向客户发出问候'''
        print("Hello, " + self.first + ' ' + self.last + "!")
        
user = User("Kaly", "Thompson", 28)
user.describe_user()
user.greet_user()

# Car类
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

# 给属性指定默认值
# 类中的每个属性都必须有初始值，即使是0或是空字符串，设定默认值时，在方法__init__内指定是可行的，且无需为它提供初始值的形参
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值
# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# 通过方法对属性值进行递增
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''里程表读数增加指定的量'''
        self.odometer_reading += miles
    
my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increase_odometer(450)
my_new_car.read_odometer()

# assigmnet9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThis restaurant's name is: " + self.name)
        print("Cuisine type: " + self.type)
        
    def open_restaurant(self):
        print("is open")
        
    def set_number_served(self, number):
        '''设置就餐人数'''
        self.number_served = number
        print("Number served: " + str(self.number_served))
        
    def increment_number_served(self, increment_number):
        '''就餐人数递增'''
        self.number_served += increment_number
        print("Number served: " + str(self.number_served))
        
restaurant = Restaurant("a", "b")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(50)
restaurant.increment_number_served(8)

# assignment9-5
class User():
    def __init__(self, first_name,last_name, age):
        '''初始化描述客户的信息'''
        self.first = first_name
        self.last = last_name
        self.age = age
        self.login_attempts = 1
        
    def describe_user(self):
        '''打印客户信息摘要'''
        print("First name: " + self.first.title())
        print("Last name: " + self.last.title())
        print("Age: " + str(self.age))
        
    def greet_user(self):
        '''向客户发出问候'''
        print("Hello, " + self.first + ' ' + self.last + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Current login attempts: " + str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Current login attempts: " + str(self.login_attempts))
    
user = User("Kaly", "Thompson", 28)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()

# 继承：一个类继承另一个类时，将自动获得另一个类的所有属性和方法
# super()是一个特殊函数，将父类和子类关联起来
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''里程表读数增加指定的量'''
        self.odometer_reading += miles
        
class ElecticCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self, make, model, year):
        '''初始化父类的属性'''
        super().__init__(make, model, year)
        
my_tesla = ElecticCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()

# 给子类定义属性和方法
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''里程表读数增加指定的量'''
        self.odometer_reading += miles
        
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        '''
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车的特有属性
        '''
        # 注意继承父类的__init__方法时不用self形参
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        '''打印描述电瓶容量的消息'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 重写父类的方法：对于父类的方法，只要不符合子类模拟的实物的行为，都可对其进行重写
# 可在子类中定义一个这样的方法，与它要重写的父类中的方法同名

# 将实例用作属性：可将大型类拆分为许多协同工作的小类
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''里程表读数增加指定的量'''
        self.odometer_reading += miles
        
class Battery():
    '''模拟电动汽车电瓶'''
    
    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size
        
    def describe_battery(self):
        '''打印描述电瓶容量的消息'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 创建一个新的Battery实例，将实例储存在属性self.battery中
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# assignment9-6
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThis restaurant's name is: " + self.name)
        print("Cuisine type: " + self.type)
        
    def open_restaurant(self):
        print("is open")
        
    def set_number_served(self, number):
        '''设置就餐人数'''
        self.number_served = number
        print("Number served: " + str(self.number_served))
        
    def increment_number_served(self, increment_number):
        '''就餐人数递增'''
        self.number_served += increment_number
        print("Number served: " + str(self.number_served))
        
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def describe_flavors(self):
        print(self.flavors)
        
flavors = ['cc', 'dd']        
restaurant = IceCreamStand("a", "b", flavors)

restaurant.describe_restaurant()
restaurant.describe_flavors()

# assignmet9-7
class User():
    def __init__(self, first_name,last_name, age):
        '''初始化描述客户的信息'''
        self.first = first_name
        self.last = last_name
        self.age = age
        self.login_attempts = 1
        
    def describe_user(self):
        '''打印客户信息摘要'''
        print("First name: " + self.first.title())
        print("Last name: " + self.last.title())
        print("Age: " + str(self.age))
        
    def greet_user(self):
        '''向客户发出问候'''
        print("Hello, " + self.first + ' ' + self.last + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Current login attempts: " + str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Current login attempts: " + str(self.login_attempts))
        
class Admin(User):
    
    def __init__(self, first_name,last_name, age, privileges):
        super().__init__(first_name,last_name, age)
        self.privileges = privileges
        
    def show_privileges(self):
        print(self.privileges)
   
privileges = ['can add post', 'can delete post', 'can be user']
user = Admin("Kaly", "Thompson", 28, privileges)
user.describe_user()
user.greet_user()
user.show_privileges()  

# assignment9-8
 class User():
    def __init__(self, first_name,last_name, age):
        '''初始化描述客户的信息'''
        self.first = first_name
        self.last = last_name
        self.age = age
        self.login_attempts = 1
        
    def describe_user(self):
        '''打印客户信息摘要'''
        print("First name: " + self.first.title())
        print("Last name: " + self.last.title())
        print("Age: " + str(self.age))
        
    def greet_user(self):
        '''向客户发出问候'''
        print("Hello, " + self.first + ' ' + self.last + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Current login attempts: " + str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Current login attempts: " + str(self.login_attempts))

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print(self.privileges)
        
class Admin(User):
    
    def __init__(self, first_name,last_name, age, privileges):
        super().__init__(first_name,last_name, age)
        self.privileges = Privileges(privileges)
        
   
privileges = ['can add post', 'can delete post', 'can be user']
user = Admin("Kaly", "Thompson", 28, privileges)
user.privileges.show_privileges()

# assignment9-9
class Car():
    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''打印汽车里程'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值
           禁止将里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increase_odometer(self, miles):
        '''里程表读数增加指定的量'''
        self.odometer_reading += miles
        
class Battery():
    '''模拟电动汽车电瓶'''
    
    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size
        
    def describe_battery(self):
        '''打印描述电瓶容量的消息'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
    def upgrade_barrery(self):
        if self.battery_size != 85:
            self.battery_size = 85     
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 创建一个新的Battery实例，将实例储存在属性self.battery中
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_barrery()
my_tesla.battery.get_range()

# 导入类
# 导入单个类
from car import Car

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# 在一个模块中储存多个类
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_barrery()
my_tesla.battery.get_range()

# 从一个模块中导入多个类
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 导入整个模块，使用句点表示法访问需要的类
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 导入模块中所有的类
from car import *

# 在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# python标准库
from collections import OrderdDict

favoriate_languages = OrderdDict()

favoriate_languages['jen'] = 'python'
favoriate_languages['sarsh'] = 'c'
favoriate_languages['edward'] = 'ruby'
favoriate_languages['phil'] = 'python'

for name, language in favoriate_languages.items():
    print(name.title() + "'s favoriate language is " + language.title() + ".")

# 类名应采用驼峰命名法，类名中每个单词首字母大写且不使用下划线，实例名和模块名都采用小写格式，并在单词之间加下划线
# 每个类都应紧跟在类定义后面包含一个文档字符串
# 在类中可使用一个空行来分隔方法，模块中可使用两个空行来分隔类
# 需要同时导入标准库的模块和编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入自己编写的模块的import语句
    







        