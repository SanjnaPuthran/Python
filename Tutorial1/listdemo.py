# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:07:03 2020

@author: soumi
"""

mylist=["one",21,"two",767]
print(mylist)
print(type(mylist))
print(mylist.insert(0,11))
print(mylist)
print(mylist.append(6611))
print("append :",mylist)

print(mylist.remove(21))
print("remove :",mylist)

print(mylist.pop(0))
print("pop :",mylist)

print("index :",mylist.index(767))

l2=[1,23,244,678,905]
mylist.extend(l2)
print("extend :",mylist)

l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
print(23 in l2)
print(l2[0:3])  #slice

l2.reverse()
print("reverse :" ,l2)




