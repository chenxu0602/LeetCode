#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (67.74%)
# Likes:    619
# Dislikes: 42
# Total Accepted:    98K
# Total Submissions: 145K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2,5,2]
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        # Depth-First Search
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # vals = []

        # def dfs(node):
        #     if node:
        #         vals.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)

        # dfs(root)
        # return len(set(vals)) == 1


        # Recursion
        # Time  complexity: O(N)
        # Space complexity: O(H)
        left_correct = (not root.left or root.val == root.left.val
                        and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                         and self.isUnivalTree(root.right))

        return left_correct and right_correct
        
# @lc code=end

