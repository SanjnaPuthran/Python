# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:42:51 2020

@author: soumi
"""

#by default open()=> opens in read mode
#for writing if file is not there it creates new file 
# for existing file it overwrites 
# for append use a

fp=open("mydata.txt","w")

fp.write("May is a beautiful month ")
fp.write("December is my favorite")
print("data written")
fp.close()

###   W+ , a+, r+

fp=open("mydata.txt","a")

fp.write("Badminton is awesome")
print("data appended")
fp.close()