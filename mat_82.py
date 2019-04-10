#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:06:04 2019
https://www.cnblogs.com/theskulls/p/4986885.html
@author: lx
"""

ls=[]
for line in open("p082_matrix.txt"):
    #print(line)
    a=line.split(',')
    a=[int(i) for i in a]
    ls.append(a)
 
 
ans=[ls[i][79] for i in range(80)]
######ans是每列的最小值。
###先向左和向下走
###向左走

#for ix in range(0,79)[::-1]:
##for j in range(0,80):###对每一个数
#    #向左
#    ans[0]+=ls[0][ix]
#    #向下
#    for ixia in range(1,80):
#        ans[ixia]=min(ans[ixia],ans[ixia-1])+ls[ixia][ix]
#    #向上
#    for ishang in range(79)[::-1]:
#        ans[ishang]=min(ans[ishang],ans[ishang+1]+ls[ishang][ix])
#print(min(ans))#260324
# 




for i in range(78,-1,-1):
    ans[0]=ans[0]+ls[0][i]
 
#向下
    for j in range(1,80):
        ans[j]=min(ans[j]+ls[j][i],ans[j-1]+ls[j][i])
 
#向上
    for j in range(78,-1,-1):
        ans[j]=min(ans[j],ans[j+1]+ls[j][i])
 
print(min(ans))

