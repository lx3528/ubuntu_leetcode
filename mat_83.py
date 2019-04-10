#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:12:59 2019
#https://www.cnblogs.com/theskulls/p/4989474.html
@author: lx
"""

import time 
def readData(filename):
    fl = open(filename)
    data =[]
    for row in fl:
        row = row.split(',')
        line = [int(i) for i in row]
        data.append(line)
    fl.close()
    return data

def next_steps(pos):
    (j,i) = pos
    if i+1<size:
        right = minnum[j,i] + data[j][i+1]
        if right< minnum[j,i+1]:
            minnum[j,i+1] = right 
            next_list.append((j,i+1))
    if j+1< size:
        down = minnum[j,i] + data[j+1][i]
        if down < minnum[j+1,i]:
            minnum[j+1,i] = down
            next_list.append((j+1,i))
    if i-1 > -1:
        left = minnum[j,i] + data[j][i-1]
        if left < minnum[j,i-1]:
            minnum[j,i-1] = left
            next_list.append((j,i-1))
    if j-1 > -1:
        up = minnum[j,i] + data[j-1][i]
        if up < minnum[j-1,i]:
            minnum[j-1,i] = up
            next_list.append((j-1,i))
   
t0 = time.time()         
filename = 'p083_matrix.txt'
data = readData(filename)
size = 80
infinity = 10**10
minnum = {}
for i in range(0,size):
    for j in range(0,size):
        minnum[j,i] = infinity 

next_list = []
            
minnum[0,0] = data[0][0]
test = [(0,0)]
while test!=[]:
    next_list = []
    for el in test:
        next_steps(el)
    test = next_list
print(minnum[size-1,size-1])
t1 = time.time()
print("running time=",(t1-t0),"s")

# 425185
# running time= 0.112999916077 s