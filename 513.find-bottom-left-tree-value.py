#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (58.80%)
# Likes:    591
# Dislikes: 103
# Total Accepted:    75.4K
# Total Submissions: 128.1K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        deq = deque([root])

        while deq:
            nodes = []
            for _ in range(len(deq)):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                else:
                    nodes.append(node)

                if node.right:
                    deq.append(node.right)
                else:
                    nodes.append(node)

        return nodes[0].val
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val
#        return queue[-1].val
        

