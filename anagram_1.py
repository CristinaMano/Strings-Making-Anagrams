# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:11:23 2020

@author: crist
"""

import math
import os
import random
import re
import sys


def Anagram(a, b):
    al=list(a) 
    aset=list(set(al)) 
    aset.sort() 

    bl=list(b)
    bset=list(set(bl)) 
    bset.sort()
    count_b=[]
    deleted=0
    for _,item in enumerate(aset): 
        counta=al.count(item) 
        countb=bl.count(item) 
        count_b.append((countb)) 
        deleted+=abs(counta-countb) 

    deleted+=len(b)-sum(count_b)
    return deleted

if __name__ == '__main__':

    a = input() # eq:use as input 'cdecac'

    b = input() # eq:use as input 'abczd'

    res = Anagram(a, b)
