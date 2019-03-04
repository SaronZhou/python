# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:55:50 2019

@author: admin
"""

def make_pizza(size, *toppings):
    '''概述要制作的披萨'''
    print("\nMakeing a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)