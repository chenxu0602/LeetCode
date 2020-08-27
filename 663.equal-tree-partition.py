#
# @lc app=leetcode id=663 lang=python3
#
# [663] Equal Tree Partition
#
# https://leetcode.com/problems/equal-tree-partition/description/
#
# algorithms
# Medium (38.91%)
# Likes:    268
# Dislikes: 22
# Total Accepted:    16.8K
# Total Submissions: 43.3K
# Testcase Example:  '[5,10,10,null,null,2,3]'
#
# 
# Given a binary tree with n nodes, your task is to check if it's possible to
# partition the tree to two trees which have the equal sum of values after
# removing exactly one edge on the original tree.
# 
# 
# Example 1:
# 
# Input:     
# ⁠   5
# ⁠  / \
# ⁠ 10 10
# ⁠   /  \
# ⁠  2   3
# 
# Output: True
# Explanation: 
# ⁠   5
# ⁠  / 
# ⁠ 10
# ⁠     
# Sum: 15
# 
# ⁠  10
# ⁠ /  \
# ⁠2    3
# 
# Sum: 15
# 
# 
# 
# 
# Example 2:
# 
# Input:     
# ⁠   1
# ⁠  / \
# ⁠ 2  10
# ⁠   /  \
# ⁠  2   20
# 
# Output: False
# Explanation: You can't split the tree into two trees with equal sum after
# removing exactly one edge on the tree.
# 
# 
# 
# Note:
# 
# The range of tree node value is in the range of [-100000, 100000].
# 1 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        seen = []

        def sum_(node):
            if not node: return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen

        
# @lc code=end

