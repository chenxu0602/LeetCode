#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (21.40%)
# Likes:    339
# Dislikes: 421
# Total Accepted:    31.3K
# Total Submissions: 147.8K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
# 
# Implement these functions in your linked list class:
# 
# 
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted. If index is negative, the node will be
# inserted at the head of the list.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
# 
# 
# Example:
# 
# 
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# 
# 
# Note:
# 
# 
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
# 
# 
#
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.len - 1: return -1        
        cur = self.head
        if 2*(index-1) > self.len:
            for i in range(self.len - index):
                cur = cur.prev
        else:
            for i in range(index):
                cur = cur.next
        return cur.val
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            p = Node(val)
            if self.len == 1:
                q = self.head
            else:
                q = self.head.prev
            q.next, p.prev = p, q
            self.head.prev, p.next = p, self.head
            self.head = p
        self.len += 1
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
        else:
            p = Node(val)
            if self.len == 1:
                q = self.head
            else:
                q = self.head.prev
            q.next, p.prev = p, q
            p.next, self.head.prev = self.head, p
        self.len += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.len: return
        if index == self.len: 
            self.addAtTail(val)
        elif not index:
            self.addAtHead(val)
        else:
            cur = self.head
            if 2 * (index - 1) > self.len:
                for i in range(self.len - index):
                    cur = cur.prev
                else:
                    for i in range(index):
                        cur = cur.next
            p = Node(val)
            q = cur.prev
            q.next, p.prev = p, q
            p.next, cur.prev = cur, p
            self.len += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.len - 1:
            return
        elif self.len == 1:
            self.head, self.len = None, 0
        else:
            cur = self.head
            if 2 * (index - 1) > self.len:
                for i in range(self.len - index):
                    cur = cur.prev
            else:
                for i in range(index):
                    cur = cur.next

            p = cur.prev
            q = cur.next
            p.next, q.prev = q, p
            self.len -= 1



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

