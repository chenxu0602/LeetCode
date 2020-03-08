#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (51.09%)
# Likes:    1367
# Dislikes: 570
# Total Accepted:    147.7K
# Total Submissions: 289.1K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# Example 1:
# 
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,4,6].
# 
# 
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.iter = iter(nestedList)
        
    
    def next(self) -> int:
        return self.nextInteger
        
    
    def hasNext(self) -> bool:
        while self.iter:
            try:
                r = next(self.iter)
            except StopIteration:
                self.iter = self.stack.pop() if self.stack else None
                continue

            if r.isInteger():
                self.nextInteger = r.getInteger()
                return True

            self.stack.append(self.iter)
            self.iter = iter(r.getList())

        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

