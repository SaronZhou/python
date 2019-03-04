# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:18:01 2019

@author: admin
"""

'''一个可用于表示燃油汽车和电动汽车的类'''
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