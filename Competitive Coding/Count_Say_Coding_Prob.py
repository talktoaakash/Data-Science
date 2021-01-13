#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:46:58 2021

@author: akashverma
"""
def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

def count_say(n):
    i=0
    s="1"
    while i<n-1:
      s = next_number(s)
      i+=1
    return(s)


