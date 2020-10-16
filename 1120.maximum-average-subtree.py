#
# @lc app=leetcode id=1120 lang=python3
#
# [1120] Maximum Average Subtree
#
# https://leetcode.com/problems/maximum-average-subtree/description/
#
# algorithms
# Medium (62.12%)
# Likes:    267
# Dislikes: 9
# Total Accepted:    18.2K
# Total Submissions: 28.9K
# Testcase Example:  '[5,6,1]'
#
# Given the root of a binary tree, find the maximum average value of any
# subtree of that tree.
# 
# (A subtree of a tree is any node of that tree plus all its descendants. The
# average value of a tree is the sum of its values, divided by the number of
# nodes.)
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [5,6,1]
# Output: 6.00000
# Explanation: 
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 5000.
# Each node will have a value between 0 and 100000.
# Answers will be accepted as correct if they are within 10^-5 of the correct
# answer.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:

        def dfs(node):
            if not node:
                return 0, 0.0

            n1, s1 = dfs(node.left)
            n2, s2 = dfs(node.right)

            n = n1 + n2 + 1
            s = s1 + s2 + node.val
            self.res = max(self.res, s / n)

            return n, s

        self.res = 0
        dfs(root)
        return self.res
        
# @lc code=end

