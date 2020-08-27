#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (43.26%)
# Likes:    402
# Dislikes: 610
# Total Accepted:    53K
# Total Submissions: 122.9K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # We know all values in the subtree at \text{node}node are at least \text{node.val}node.val, so there cannot be a better candidate for the second minimum in this subtree. 
        # Time  complexity: O(N)
        # Space complexity: O(N)
        self.ans = float("inf")
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float("inf") else -1
        

