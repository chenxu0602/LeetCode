#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
# https://leetcode.com/problems/design-skiplist/description/
#
# algorithms
# Hard (57.25%)
# Likes:    77
# Dislikes: 12
# Total Accepted:    2.2K
# Total Submissions: 3.8K
# Testcase Example:  '["Skiplist","add","add","add","search","add","search","erase","erase","search"]\r' + '\n[[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]\r'
#
# Design a Skiplist without using any built-in libraries.
# 
# A Skiplist is a data structure that takes O(log(n)) time to add, erase and
# search. Comparing with treap and red-black tree which has the same function
# and performance, the code length of Skiplist can be comparatively short and
# the idea behind Skiplists are just simple linked lists.
# 
# For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to
# add 80 and 45 into it. The Skiplist works this way:
# 
# 
# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
# 
# You can see there are many layers in the Skiplist. Each layer is a sorted
# linked list. With the help of the top layers, add , erase and search can be
# faster than O(n). It can be proven that the average time complexity for each
# operation is O(log(n)) and space complexity is O(n).
# 
# To be specific, your design should include these functions:
# 
# 
# bool search(int target) : Return whether the target exists in the Skiplist or
# not.
# void add(int num): Insert a value into the SkipList. 
# bool erase(int num): Remove a value in the Skiplist. If num does not exist in
# the Skiplist, do nothing and return false. If there exists multiple num
# values, removing any one of them is fine.
# 
# 
# See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list
# 
# Note that duplicates may exist in the Skiplist, your code needs to handle
# this situation.
# 
# 
# 
# Example:
# 
# 
# Skiplist skiplist = new Skiplist();
# 
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0);   // return false.
# skiplist.add(4);
# skiplist.search(1);   // return true.
# skiplist.erase(0);    // return false, 0 is not in skiplist.
# skiplist.erase(1);    // return true.
# skiplist.search(1);   // return false, 1 has already been erased.
# 
# 
# Constraints:
# 
# 
# 0 <= num, target <= 20000
# At most 50000 calls will be made to search, add, and erase.
# 
#

# @lc code=start
import math
from random import random

class Node:
    __slots__ = "val", "levels"
    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels

class Skiplist:

    def __init__(self):
       self.head = Node(-1, 16) 

    def _iter(self, num):
        cur = self.head
        for level in range(15, -1, -1):
            while True:
                future = cur.levels[level]
                if future and future.val < num:
                    cur = future
                else:
                    break
            yield cur, level

    def search(self, target: int) -> bool:
        for prev, level in self._iter(target):
            pass
        cur = prev.levels[0]
        return cur and cur.val == target
        
    def add(self, num: int) -> None:
        nodevls = min(16, 1+int(math.log2(1.0 / random())))
        node = Node(num, nodevls)

        for cur, level in self._iter(num):
            if level < nodevls:
                future = cur.levels[level]
                cur.levels[level] = node
                node.levels[level] = future
        
    def erase(self, num: int) -> bool:
        ans = False
        for cur, level in self._iter(num):
            future = cur.levels[level]
            if future and future.val == num:
                ans = True
                cur.levels[level] = future.levels[level]
        return ans
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end

