#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (34.08%)
# Likes:    1054
# Dislikes: 268
# Total Accepted:    64.2K
# Total Submissions: 187.5K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        def dfs(node, prev_val):
            if node is None:
                return 0
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            self.max_val = max(self.max_val, left+right)
            if node.val == prev_val:
                return max(left, right) + 1
            return 0

        self.max_val = 0
        if root is None:
            return 0
        dfs(root, root.val)
        return self.max_val
        """

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            l = r = 0
            if node.left and node.left.val == node.val:
                l = left + 1
            if node.right and node.right.val == node.val:
                r = right + 1
            self.ans = max(self.ans, l + r)
            return max(l, r)

        self.ans = 0
        dfs(root)
        return self.ans
        

