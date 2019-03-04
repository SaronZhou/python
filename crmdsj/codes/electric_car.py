# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:28:44 2019

@author: admin
"""
from car import Car

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