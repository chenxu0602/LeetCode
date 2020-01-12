#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (47.18%)
# Likes:    341
# Dislikes: 787
# Total Accepted:    54.9K
# Total Submissions: 116.4K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference between the sum
# of all left subtree node values and the sum of all right subtree node values.
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# 
# Input: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# 
# 
# Note:
# 
# The sum of node values in any subtree won't exceed the range of 32-bit
# integer. 
# All the tilt values won't exceed the range of 32-bit integer.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        def dfs(node):
            if not node:
                return 0
            a, b = dfs(node.left), dfs(node.right)
            self.s += abs(a - b)
            return a + b + node.val

        self.s = 0
        dfs(root)
        return self.s
        """

        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            return left[0]+right[0]+node.val, abs(left[0]-right[0]) + left[1] + right[1]

        return dfs(root)[1]
        

