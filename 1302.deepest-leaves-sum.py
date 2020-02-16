#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (83.69%)
# Likes:    175
# Dislikes: 17
# Total Accepted:    16.3K
# Total Submissions: 19.5K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
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
    def deepestLeavesSum(self, root: TreeNode) -> int:

        q = [root]
        while q:
            pre, q = q, [child for p in q for child in (p.left, p.right) if child]
        return sum(node.val for node in pre)
        
# @lc code=end

