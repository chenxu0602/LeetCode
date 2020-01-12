#
# @lc app=leetcode id=339 lang=python3
#
# [339] Nested List Weight Sum
#
# https://leetcode.com/problems/nested-list-weight-sum/description/
#
# algorithms
# Easy (68.35%)
# Likes:    298
# Dislikes: 68
# Total Accepted:    57.7K
# Total Submissions: 84.3K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, return the sum of all integers in the list
# weighted by their depth.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: 10 
# Explanation: Four 1's at depth 2, one 2 at depth 1.
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: 27 
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 +
# 4*2 + 6*3 = 27.
# 
# 
# 
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def dfs(self, nestedList: List[NestedInteger], depth: int) -> int:
        sum = 0

        for item in nestedList:
            if item.isInteger():
                sum += item.getInteger() * depth
            else:
                sum += self.dfs(item.getList(), depth + 1)

        return sum


    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        return self.dfs(nestedList, 1)
        """

        depth, ret = 1, 0
        while nestedList:
            ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        return ret
        

