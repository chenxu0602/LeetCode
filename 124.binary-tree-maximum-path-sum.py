#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (30.63%)
# Likes:    2026
# Dislikes: 153
# Total Accepted:    225.8K
# Total Submissions: 727.7K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:

        # def maxsums(node):
        #     if not node:
        #         return [-2**31] * 2
        #     left = maxsums(node.left)
        #     right = maxsums(node.right)
        #     return [node.val + max(left[0], right[0], 0),
        #             max(left + right + [node.val + left[0] + right[0]])]
        # return max(maxsums(root))

        def max_gain(node):
            nonlocal max_sum
            if not node: return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_newpath = node.val + left_gain + right_gain

            max_sum = max(max_sum, price_newpath)

            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum
        

