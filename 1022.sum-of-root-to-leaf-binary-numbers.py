#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (58.74%)
# Likes:    181
# Dislikes: 61
# Total Accepted:    20K
# Total Submissions: 32.8K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        """
        def dfs(node, path=None):
            if path is None:
                path = ""
            if node:
                path += str(node.val)
                if node.left or node.right:
                    return dfs(node.left, path) + dfs(node.right, path)
                else:
                    return int(path, 2)
            else:
                return 0
        return dfs(root)
        """

        """
        def dfs(node, parent_sum=None):
            if parent_sum == None:
                parent_sum = 0
            if node:
                parent_sum = parent_sum * 2 + node.val
                if node.left or node.right:
                    return dfs(node.left, parent_sum) + dfs(node.right, parent_sum)
                else:
                    return parent_sum
            else:
                return 0
        return dfs(root)
        """

        def dfs(node, val=0):
            if not node: return 0
            val = val * 2 + node.val
            if node.left == node.right:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root)

