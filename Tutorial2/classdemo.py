# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:00:45 2020

@author: soumi
"""

'''
Class variables are by default static
By default everything in python is public 
__ before the variable names makes it private

init is like constructor

whenever object is created init is called
self is like 'this' keyword in java

any variable declared using self is instance variable 
company name is static variable

'''


class Emp:
    companyname="SP_learing"
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        print("Inside Init ",eid,ename)
        
# the first parameter in method always has to be self 
    
    def info(self):
        print("Inside info :",self.eid,self.ename)

##################################3
        
print (Emp.companyname)
## creating an object 
obj=Emp(1,"Sanjna")
obj.info()        
        