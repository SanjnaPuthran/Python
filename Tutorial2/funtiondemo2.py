# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:04:02 2020

@author: soumi
"""

#functions with default parameter values
#always use mandatory paramter first then followed by default paramaters values 

def sum(num1,num2,num3=0):
    print("The value is ", num1+num2+num3)
    
sum(5,6)
sum(5,6,8)


#when we try to overload method
#it fails because the first method defination gets overriden by the second one    

def sum():
    print("Check method ")
    
sum()
#sum(5,6)    



#correct way of doing in python

def sum3(*val):
    print("The value is ",val)
    sum=0
    for data in val:
        sum=sum+data
    print(sum)


sum3(1,5,5)
sum3(1,5)
sum3(1,5,80)    