# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:18:52 2020

@author: soumi
"""

'''
set is mutable
You can make changes to it
Does not allow duplicate 
Linked list is used in sets
no indexing
order not maintained

'''

##set() SET{}

myset={12,34,6,67,6,346,3}
print(myset)
myset.add(245)
print(myset)
myset.remove(12)
print(myset)


set1={"SET" ,10,22,384}
set2={"SET" ,10}
print("Union: ",set1.union(set2))
print("Intersection: ",set1.intersection(set2))
print("Diffrence: ",set1.difference(set2))
print("symmetric_difference: ",set1.symmetric_difference(set2))
print("issuperset: ",set1.issuperset(set2))
print("issuperset reverse: ",set1.issuperset(set2))
