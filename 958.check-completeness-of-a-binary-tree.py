#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (48.32%)
# Likes:    366
# Dislikes: 8
# Total Accepted:    24.5K
# Total Submissions: 49.9K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a binary tree, determine if it is a complete binary tree.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
# 
# 
# 
# 
# 
# Note:
# 
# 
# The tree will have between 1 and 100 nodes.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # O(N)

        if not root: return True

        res, queue = [], deque([(root, 1)])
        while queue:
            node, pos = queue.popleft()
            res.append(pos)
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        return len(res) == res[-1]
        

