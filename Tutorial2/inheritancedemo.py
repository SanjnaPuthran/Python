# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:26:13 2020

@author: soumi
"""

class Person:
    def pinfo(self):
        print("Person Info")
    
class Emp(Person):  ## inheritance ==> emp is clid of person
    companyname="SP"
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        print("Inside Init",eid,ename)
        super().pinfo() 
        
    def info(self):
        print("Emp Info :",self.eid,self.ename)
            
            
            
#######################
            
print(Emp.companyname)

##creating an object

obj=Emp(1,"Sam")            
obj.info()
obj.pinfo()