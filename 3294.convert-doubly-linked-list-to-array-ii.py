#
# @lc app=leetcode id=3294 lang=python3
#
# [3294] Convert Doubly Linked List to Array II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:

        while node.prev:
            node = node.prev

        res = []
        while node:
            res += node.val,
            node = node.next

        return res
        
# @lc code=end

