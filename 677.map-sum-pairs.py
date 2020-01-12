#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (51.85%)
# Likes:    318
# Dislikes: 61
# Total Accepted:    28.3K
# Total Submissions: 54.3K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n' +
#
# 
# Implement a MapSum class with insert, and sum methods.
# 
# 
# 
# For the method insert, you'll be given a pair of (string, integer). The
# string represents the key and the integer represents the value. If the key
# already existed, then the original key-value pair will be overridden to the
# new one.
# 
# 
# 
# For the method sum, you'll be given a string representing the prefix, and you
# need to return the sum of all the pairs' value whose key starts with the
# prefix.
# 
# 
# Example 1:
# 
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
# 
# 
# 
#
from collections import Counter

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.score = Counter()
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key)+1):
            prefix = key[:i]
            self.score[prefix] += delta
        
    def sum(self, prefix: str) -> int:
        return self.score[prefix]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

