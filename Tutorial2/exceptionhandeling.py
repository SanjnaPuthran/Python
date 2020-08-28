# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:34:37 2020

@author: soumi
"""

#custom exception 

#class myexp(Exception):
 #   def __init__(self):
  #      print("My exception")
#raise myexp

try:
    num1=10
    num2=0
    ans=num1/num2
    print(ans)
#except myexp as mye:
#print("Hello")

except ValueError as ae:
    print("Value input error: ",ae) 
except ZeroDivisionError as ze:
    print("Divide by zeror error: ",ze) 
except Exception as e:
    print("Error: ",e)            
finally:
    print("finally")    
        