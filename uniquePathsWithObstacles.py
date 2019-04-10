#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:46:43 2019

@author: lx
"""
#https://leetcode.com/problems/unique-paths-ii/discuss/23248/My-C%2B%2B-Dp-solution-very-simple!
class Solution:
#    def uniquePathsWithObstacles(self, obstacleGrid):
#        #print(obstacleGrid)
#        #return
#        m=len(obstacleGrid)
#        n=len(obstacleGrid[0])
#        if m==1 and n==1 and obstacleGrid[0][0]==1:return 0
#        dp=[[0 for _ in range(n)] for _ in range(m)]
#        dp[0][0]=1
#        #for j in range(n):
#            #dp[0][j]=1
#        for i in range(0,m):
#            #dp[i][0]=1
#            for j in range(0,n):
#                if obstacleGrid[i][j]!=1:
#                    if i-1>=0 and i<m and obstacleGrid[i-1][j]!=1:##多加0 pading就不用判断了
#                        dp[i][j]+=dp[i-1][j]
#                    if j-1>=0 and j<n and obstacleGrid[i][j-1]!=1:
#                        dp[i][j]+=dp[i][j-1]
#        return dp[-1][-1]
  #40ms----13.3mb
    def uniquePathsWithObstacles(self, obstacleGrid):
        #print(obstacleGrid)
        #return
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==1 and n==1 and obstacleGrid[0][0]==1:return 0
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            dp[i][0]=1
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    if obstacleGrid[i-1][j]!=1:
                        dp[i][j]+=dp[i-1][j]
                    if obstacleGrid[i][j-1]!=1:
                        dp[i][j]+=dp[i][j-1]
        return dp[-1][-1]
pp=Solution()

print(pp.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]]))

