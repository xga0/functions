#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:42:52 2020

@author: seangao
"""

def countFrequency(list):
    import pandas as pd
    from collections import Counter
    
    value_counts = Counter(list)
    vc = value_counts.most_common()
    vc = pd.DataFrame(vc)
    
    return vc

#TEST
    
import random

grades = []
for i in range(0, 100):
    n = random.randint(55, 100)
    grades.append(n)
    
df = countFrequency(grades)

df.head(5)
    