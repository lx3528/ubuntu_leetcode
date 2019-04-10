#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:19:12 2019

@author: lx
还是错的---f×××
改了好多遍---等于号，边界考虑，负数--终于过了
"""
class listnode:###单链表形式写一遍
    def __init__(self,val):
        self.val=val;
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.linkedlist=None
        self.size=0
    def get(self, index: int):
        #print('get'+str(index))
        #self.print_list()
        if index>self.size or index<0:
            return -1
        if self.linkedlist is None:
            return -1

        curr=self.linkedlist
#            for i in range(index):
#                curr = curr.next
#            return curr.val
        while index>0:
            curr=curr.next
            index-=1
        return curr.val
    def addAtHead(self, val: int) :

        temp=listnode(val)
        temp.next=self.linkedlist
        self.linkedlist=temp
        self.size+=1

    def addAtTail(self, val: int) :
        """
        Append a node of value val to the last element of the linked list.
        """
        temp1=self.linkedlist
        if temp1 is None:
            self.linkedlist=listnode(val)
            
        else:
            while temp1.next is not None:
                temp1=temp1.next
            temp1.next=listnode(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) : #-1?
        #self.print_list()
        #print(self.size)
        if index>self.size :
            return 
        if index<=0:
            temp2=listnode(val)
            temp2.next = self.linkedlist
            self.linkedlist = temp2
            self.size+=1   
        elif index==0:
            self.addAtHead(val)
        else:
            temp1=self.linkedlist
            while index -1>0:###出错的
                temp1=temp1.next;
                index-=1
            temp2=listnode(val)
            temp2.next=temp1.next
            temp1.next=temp2
            self.size+=1   
        #self.print_list()

    def deleteAtIndex(self, index: int):
        if index>=self.size or index<0:
            return 
        else:
            temp=self.linkedlist
            if index==0:
                self.linkedlist=self.linkedlist.next
            else:
                while index-1>0:
                    
                    temp=temp.next
                    index-=1
                temp.next=temp.next.next
            self.size-=1  
        return 
    def print_list(self):
        temp=self.linkedlist
        while temp:
            print(str(temp.val)+'->')
            temp=temp.next
#["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
#[[],[1],[3],[1,2],[1],[1],[1]]
        
    
obj = MyLinkedList()

#print(obj.addAtHead(1));
#print(obj.addAtTail(3))
#print(obj.addAtIndex(1, 2))  # linked list becomes 1->2->3
#print(obj.get(1))      # returns 2
#print(obj.deleteAtIndex(1))  # now the linked list is 1->3
#print(obj.get(1))

print(obj.addAtHead(1));

print(obj.addAtIndex(1, 2))  # linked list becomes 1->2->3
print(obj.get(1))      # returns 2
print(obj.get(0))  # now the linked list is 1->3
print(obj.get(2))   


print(obj.addAtHead(1));

print(obj.addAtIndex(1, 2))  # linked list becomes 1->2->3
print(obj.get(1))      # returns 2
print(obj.get(0))  # now the linked list is 1->3
print(obj.get(2))   