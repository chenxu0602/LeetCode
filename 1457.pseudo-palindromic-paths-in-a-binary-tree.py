#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
#
# algorithms
# Medium (67.91%)
# Likes:    328
# Dislikes: 12
# Total Accepted:    20.5K
# Total Submissions: 30.2K
# Testcase Example:  '[2,3,1,3,1,null,1]'
#
# Given a binary tree where node values are digits from 1 to 9. A path in the
# binary tree is said to be pseudo-palindromic if at least one permutation of
# the node values in the path is a palindrome.
# 
# Return the number of pseudo-palindromic paths going from the root node to
# leaf nodes.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the red path [2,3,3], the
# green path [2,1,1], and the path [2,3,1]. Among these paths only red path and
# green path are pseudo-palindromic paths since the red path [2,3,3] can be
# rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be
# rearranged in [1,2,1] (palindrome).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the green path [2,1,1],
# the path [2,1,3,1], and the path [2,1]. Among these paths only the green path
# is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1]
# (palindrome).
# 
# 
# Example 3:
# 
# 
# Input: root = [9]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.
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
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(K + H)
        # def dfs(node, count=0):
        #     if not node: return 0
        #     count ^= 1 << (root.val - 1)
        #     res = dfs(root.left, count) + dfs(root.right, count)
        #     if root.left is root.right:
        #         if count & (count - 1) == 0:
        #             res += 1
        #     return res

        # return dfs(root)


        def preorder(node, cnt):
            if not node: return 0
            cnt ^= 1 << node.val
            if node.left is node.right:
                return 1 if cnt & (cnt - 1) == 0 else 0

            return preorder(node.left, cnt) + preorder(node.right, cnt)

        return preorder(root, 0)

            



        
# @lc code=end

