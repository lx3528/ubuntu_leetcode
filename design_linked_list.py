#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:32:38 2019

@author: lx
"""
####出错了，我再写个多链表的
class listnode:###单链表形式写一遍
    def __init__(self,val):
        self.val=val;
        self.next=None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist=listnode(0)
        self.size=0;

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.size==0:
            return -1
        if index>=self.size:
            return -1
        else:
            temp=self.linkedlist
            while index-1>0:
                temp=temp.next
                index-=1
            return temp.val
    def addAtHead(self, val: int) :
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp=listnode(val)
        temp.next=self.linkedlist
        self.linkedlist=temp
        self.size+=1

    def addAtTail(self, val: int) :
        """
        Append a node of value val to the last element of the linked list.
        """
        temp=self.size-1;temp1=self.linkedlist
        if temp==-1:
            self.addAtHead(val)
        else:
            while temp1.next.next is not None:
                temp1=temp1.next
            temp2=temp1.next;
            temp1.next=listnode(val)
            temp1.next.next=temp2;
#            while temp-1 >0:
#                temp1=temp1.next;
#                temp-=1
#            temp2=listnode(val)
#            temp2.next=temp1.next
#            temp1.next=temp2
            self.size+=1

    def addAtIndex(self, index: int, val: int) :
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index>=self.size:
            return 
        temp=index;temp1=self.linkedlist
        if temp==0:
            self.addAtHead(val)
        else:
            while temp-1 >0:
                temp1=temp1.next;
                temp-=1
            temp2=listnode(val)
            temp2.next=temp1.next
            temp1.next=temp2
            self.size+=1        

    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index>=self.size:
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
                    
            return 


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

print(obj.addAtHead(1));
print(obj.addAtTail(3))
print(obj.addAtIndex(1, 2))  # linked list becomes 1->2->3
print(obj.get(1))      # returns 2
print(obj.deleteAtIndex(1))  # now the linked list is 1->3
print(obj.get(1))










