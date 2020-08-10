#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#
# https://leetcode.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (35.72%)
# Likes:    623
# Dislikes: 60
# Total Accepted:    46.9K
# Total Submissions: 130.8K
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return float("inf"), float("-inf"), 0

            left, right = map(dfs, (node.left, node.right))

            if left[1] < node.val < right[0]:
                return min(node.val, left[0]), max(node.val, right[1]), left[2] + right[2] + 1
            else:
                return float("-inf"), float("inf"), max(left[2], right[2])

        return dfs(root)[2]

        
        
# @lc code=end

