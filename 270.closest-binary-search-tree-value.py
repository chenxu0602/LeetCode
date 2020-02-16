#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (43.88%)
# Likes:    395
# Dislikes: 30
# Total Accepted:    87.9K
# Total Submissions: 200.3K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: 4
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
    def closestValue(self, root: TreeNode, target: float) -> int:

        # def inorder(node):
        #     return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        # return min(inorder(root), key=lambda x: abs(target - x))

        # stack, pred = [], float("-inf")

        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left 
        #     root = stack.pop()

        #     if pred <= target < root.val:
        #         return min(pred, root.val, key=lambda x: abs(target-x))

        #     pred = root.val
        #     root = root.right

        # return pred

        # res = root.val
        # while root:
        #     if abs(root.val - target) < abs(target - res):
        #         res = root.val

        #     root = root.left if target < root.val else root.right
        # return res

        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target-x))
            root = root.left if target < root.val else root.right
        return closest


