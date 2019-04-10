#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:01:19 2019
#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/
@author: lx
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #temp=ListNode(0);
        if not head:return head
        size=0;
        temp=head;
        global node
        node=head;
        
        while temp:
            temp=temp.next
            size+=1
        return self.tobst(0,size-1)
    
    
    def tobst(self,left,right):
        
        if right<left:
            return None
        else:
            global node
            if not node:
                return node
            mid=(right+left)//2
            zhong_left=self.tobst(left,mid-1)
            
            zhong=TreeNode(node.val)
            zhong.left=zhong_left
            
            node=node.next
            zhong_right=self.tobst(mid+1,right)
            zhong.right=zhong_right
            
            return zhong
#[-10,-3,0,5,9]
tt1=ListNode(0)
pre=tt1
for i in [-10,-3,0,5,9]:
    tt1.next=ListNode(i)
    tt1=tt1.next
pp=Solution()
print(pp.sortedListToBST(pre.next))            
            
            
            
        
