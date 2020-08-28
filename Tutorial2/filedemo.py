# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:42:51 2020

@author: soumi
"""

#by default open()=> opens in read mode

fp=open("data.txt")
print(fp.read())
fp.seek(0)  #bring pointer to first line of the txt file
print (fp.readline())
print (fp.readlines())
#fp=open("C:\\Users\\data.txt")
#fp=open(r"C:\Users\data.txt")
 