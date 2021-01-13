#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:55:04 2020

@author: akashverma
"""

def MaxDistToCLosest(seats):
    n=len(seats)
    empt,result,pos1,pos2=0,0,-1,-1
    for i in range(n):
        if seats[i]==1:
            empt=0
            if pos1==-1:
                pos1=i
            pos2=i
        else:
            empt+=1
            result=max(result,(empt+1)//2)
    result=max(result,pos1,n-1-pos2)
    return result

MaxDistToCLosest([1,0,0,0,1,0,1])