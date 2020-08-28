# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:26:30 2020

@author: soumi
"""

mydict={125:"Sam",627:"Dean",826:"Rachel",927:"Joey"}
print(mydict)
print(mydict.get(627))

mydict[125]="Monika"
mydict[627]="Chandler"
print(mydict)

print("Joey" in mydict.values())
print(627 in mydict)
print(mydict.keys())
