# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:26:13 2020

@author: soumi
"""

class Person:
    def pinfo(self):
        print("Person Info")


class Human:
    def pinfo(self):
        print("Human Info")        
    
class Emp(Person,Human):  ##multiple inheritance ==> emp is clid of person
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
print("obj.info() ")        
obj.info()
print("obj.pinfo() ")        
obj.pinfo() #depending on the order of inheritance in Emp class==>> pinfo will be called >
# in this case person is first so Person info is called
