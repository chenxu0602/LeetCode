#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#
# https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
#
# algorithms
# Medium (67.78%)
# Likes:    763
# Dislikes: 25
# Total Accepted:    21.5K
# Total Submissions: 31.6K
# Testcase Example:  '[3,0,0]'
#
# Given the root of a binary tree with N nodes, each node in the tree has
# node.val coins, and there are N coins total.
# 
# In one move, we may choose two adjacent nodes and move one coin from one node
# to another.  (The move may be from parent to child, or from child to
# parent.)
# 
# Return the number of moves required to make every node have exactly one
# coin.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child,
# and one coin to its right child.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root
# [taking two moves].  Then, we move one coin from the root of the tree to the
# right child.
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: [1,0,2]
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# 
# 
# Input: [1,0,0,null,3]
# Output: 4
# 
# 
# 
# 
# Note:
# 
# 
# 1<= N <= 100
# 0 <= node.val <= N
# 
# 
# 
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
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
        

