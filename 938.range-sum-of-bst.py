#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (79.11%)
# Likes:    774
# Dislikes: 153
# Total Accepted:    146.8K
# Total Submissions: 185.5K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
# 
# The binary search tree is guaranteed to have unique values.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
# 
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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        # if root is None: return 0
        # if root.val > R: return self.rangeSumBST(root.left, L, R)
        # if root.val < L: return self.rangeSumBST(root.right, L, R)
        # return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

        # def dfs(node):
        #     if node:
        #         if L <= node.val <= R:
        #             self.ans += node.val
        #         if L < node.val:
        #             dfs(node.left)
        #         if R > node.val:
        #             dfs(node.right)

        # self.ans = 0
        # dfs(root)
        # return self.ans

        ans = 0
        stack = [root,]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if R > node.val:
                    stack.append(node.right)
        return ans
        
# @lc code=end

