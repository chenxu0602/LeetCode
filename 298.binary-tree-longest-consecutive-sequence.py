#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
#
# algorithms
# Medium (44.07%)
# Likes:    308
# Dislikes: 76
# Total Accepted:    61.6K
# Total Submissions: 139.7K
# Testcase Example:  '[1,null,3,2,4,null,null,null,5]'
#
# Given a binary tree, find the length of the longest consecutive sequence
# path.
# 
# The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The longest consecutive path
# need to be from parent to child (cannot be the reverse).
# 
# Example 1:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   / \
# ⁠  2   4
# ⁠       \
# ⁠        5
# 
# Output: 3
# 
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# 
# Example 2:
# 
# 
# Input:
# 
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠   / 
# ⁠  2    
# ⁠ / 
# ⁠1
# 
# Output: 2 
# 
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node, parent, length=0):
            if not node: return length

            if parent and parent.val + 1 == node.val:
                length += 1
            else:
                length = 1

            return max(length, dfs(node.left, node, length), dfs(node.right, node, length))

        return dfs(root, None)

            

