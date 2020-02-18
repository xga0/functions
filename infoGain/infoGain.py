# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:19:55 2020

@author: sgaox
"""

import numpy as np
import pandas as pd
import math

def infoGain2class(num_1class, num_2class):
    
    c1 = (num_1class / (num_1class + num_2class))
    p1 = -c1 * math.log(c1,2)
    
    c2 = (num_2class / (num_1class + num_2class))
    p2 = -c2 * math.log(c2,2)
    
    infoGain = p1 + p2
    return infoGain 

def infoSplit2class(list_num_each_class_each_split):

    my_list = list_num_each_class_each_split
    n_row = int(len(my_list) / 2)
    df = pd.DataFrame(np.array(my_list).reshape(n_row,2))
    
    infoSplitList = []
    for index, row in df.iterrows():
        if row[0] == 0 or row[1] == 0:
            infoSplit = 0
            infoSplitList.append(infoSplit)
        else:
            p1 = (row[0] + row[1]) / sum(my_list)
            p2 = infoGain2class(row[0], row[1])
            infoSplit = p1 * p2
            infoSplitList.append(infoSplit)
            
    infoSplit = sum(infoSplitList)
    return infoSplit

def Gain(infoGain2class, infoSplit2class):
    
    Gain = infoGain2class - infoSplit2class
    return Gain