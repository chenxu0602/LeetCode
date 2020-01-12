#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#
# https://leetcode.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (33.08%)
# Likes:    346
# Dislikes: 36
# Total Accepted:    31K
# Total Submissions: 93.4K
# Testcase Example:  '[10,5,15,1,8,null,7]'
#
# Given a binary tree, find the largest subtree which is a Binary Search Tree
# (BST), where largest means subtree with largest number of nodes in it.
# 
# Note:
# A subtree must include all of its descendants.
# 
# Example:
# 
# 
# Input: [10,5,15,1,8,null,7]
# 
# ⁠  10 
# ⁠  / \ 
# ⁠ 5  15 
# ⁠/ \   \ 
# 1   8   7
# 
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
# ⁠            The return value is the subtree's size, which is 3.
# 
# 
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """
        def dfs(root):
            if not root:
                return 0, 0, float("inf"), float("-inf")

            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)

            n = n1 + 1 + n2 if max1 < root.val < min2 else float("-inf")
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)

        return dfs(root)[0]
        """

        def dfs(node):
            if not node:
                return 0, 0, float("inf"), float("-inf")

            N1, n1, min1, max1 = dfs(node.left)
            N2, n2, min2, max2 = dfs(node.right)

            n = n1 + n2 + 1 if max1 < node.val < min2 else float("-inf")
            return max(N1, N2, n), n, min(min1, node.val), max(max2, node.val)

        return dfs(root)[0]
        

