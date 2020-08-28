# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:56:29 2020

@author: soumi
"""

def add():
    print("Inside add function ")
    
add()    


def sub(num1,num2):
    if type(num1)==int and type(num2)==int:
        print("The sum is :",num1+num2)
    if type(num1)==str and type(num2)==str:
        print("The Contactination is :",num1+num2)    
    
    
sub(10,5)
sub("Name: ","Sam")
sub(10,[10.3,45])