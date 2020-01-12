#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (68.02%)
# Likes:    331
# Dislikes: 41
# Total Accepted:    46K
# Total Submissions: 67.4K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# Return its postorder traversal as: [5,6,3,2,4,1].
# 
# 
# Note:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []

        """
        stack, result = [root,], []
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children)

        return result[::-1]
        """

        if not root.children:
            return [root.val]

        l = []
        for c in root.children:
            l += self.postorder(c)

        return l + [root.val]

        

