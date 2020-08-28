# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:39:43 2020

@author: soumi
"""

#lymbda==>one line function
#anonymous => no name to the function
#functions can be stored as a variable

add=lambda n1,n2:n1+n2

print(add(10,20))
print(type(add))

##advantage of lymbda programming is its funcational programming

def info(n1,n2,opr):
    print(opr(n1,n2))
    
    
info(10,30,add)

#lymbda can have default values

sub= lambda n1=9,n2=1:n1-n2

print(sub(10,20))
print(type(sub))
    
def info(n1,n2,opr):
    print(opr())


info(10,30,sub)