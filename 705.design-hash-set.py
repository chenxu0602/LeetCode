#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (54.37%)
# Likes:    153
# Dislikes: 41
# Total Accepted:    25.2K
# Total Submissions: 45.8K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
# 
# 
# 
# Example:
# 
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
# 
# 
#
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.m = [None] * self.size
        
    def add(self, key: int) -> None:
        index = key % self.size
        if self.m[index] is None:
            self.m[index] = ListNode(key, True)
        else:
            currNode = self.m[index]
            tempHead = currNode
            self.m[index] = ListNode(key, True)
            self.m[index].next = currNode

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.m[index] is None:
            return
        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    currNode.val = False
                    break
                currNode = currNode.next
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        if self.m[index] is None:
            return False
        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    if currNode.val is True:
                        return True
                    else:
                        return False
                currNode = currNode.next
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

