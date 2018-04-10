#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:47:31 2018

@author: beaubritain
"""
import pandas as pd
import os 
import re


os.chdir("/Users/beaubritain/Desktop/lecture_notes/Distributed")

columns = []
users = []

with open("output.txt") as f:
    for line in f:      
        new_line = line.split("    ")
        new_user = re.sub(r'^"', '', new_line[0])
        new_article = re.sub(r'\"(.*)','', new_line[1])
        users.append(new_user)
        columns.append(new_article.rstrip())
        
        
#make users unique
users = list(set(users))
columns = list(set(columns))
    
df_ = pd.DataFrame(index = users, columns=columns)
df_ = df_.fillna(0)


with open("output.txt") as f:
    for line in f:  
        new_line = line.split()
        new_user = re.sub(r'^"', '', new_line[0])
        new_article = re.sub(r'\"(.*)','', new_line[1])
        df_.loc[new_user, new_article] = new_line[2]
 

df_.to_csv('user_vectors.csv', sep='\t', encoding='utf-8')



