#
# @lc app=leetcode id=1430 lang=python3
#
# [1430] Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
#
# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/
#
# algorithms
# Medium (44.97%)
# Likes:    76
# Dislikes: 6
# Total Accepted:    35.4K
# Total Submissions: 78.7K
# Testcase Example:  '[0,1,0,0,1,0,null,null,1,0,0]\n[0,1,0,1]'
#
# Given a binary tree where each path going from the root to any leaf form a
# valid sequence, check if a given string is a valid sequence in such binary
# tree. 
# 
# We get the given string from the concatenation of an array of integers arr
# and the concatenation of all values of the nodes along a path results in a
# sequence in the given binary tree.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation: 
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
# Other valid sequences are: 
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false 
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a
# sequence.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid
# sequence.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5000
# 0 <= arr[i] <= 9
# Each node's value is between [0 - 9].
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
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, arr, depth=0):
            if not root and depth < len(arr):
                return False

            if depth == len(arr) - 1:
                return root.val == arr[depth] and not root.left and not root.right

            return root.val == arr[depth] and (dfs(root.left, arr, depth + 1) or dfs(root.right, arr, depth + 1))

        return dfs(root, arr)
        
# @lc code=end

