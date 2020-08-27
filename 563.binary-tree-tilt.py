#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (48.66%)
# Likes:    544
# Dislikes: 1332
# Total Accepted:    80.1K
# Total Submissions: 164.3K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference between the sum
# of all left subtree node values and the sum of all right subtree node values.
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# 
# Input: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# 
# 
# Note:
# 
# The sum of node values in any subtree won't exceed the range of 32-bit
# integer. 
# All the tilt values won't exceed the range of 32-bit integer.
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
    def findTilt(self, root: TreeNode) -> int:
        # O(n) / O(n)
        # def dfs(node):
        #     if not node: 
        #         return 0, 0

        #     left, right = map(dfs, (node.left, node.right))
        #     return left[0] + right[0] + node.val, abs(left[0] - right[0]) + left[1] + right[1]

        # return dfs(root)[1]


        def dfs(node):
            if not node:
                return 0

            left, right = map(dfs, (node.left, node.right))
            self.s += abs(left - right)
            return left + right + node.val

        self.s = 0
        dfs(root)
        return self.s
        
# @lc code=end

