# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:11:28 2020

@author: soumi
"""

## cmd command

##python importdemo.py 10 20 30

#output: Hello World [importdemo.py, 10, 20, 30]

import sys

print ("Hello World",sys.argv) ## command line values 
print(__name__)


def add():
    print("Add From import")

