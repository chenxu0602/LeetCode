#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description/
#
# algorithms
# Medium (45.50%)
# Likes:    292
# Dislikes: 133
# Total Accepted:    13.5K
# Total Submissions: 29.5K
# Testcase Example:  '[1,2]\n[2,1]'
#
# Given a binary tree with N nodes, each node has a different value from {1,
# ..., N}.
# 
# A node in this binary tree can be flipped by swapping the left child and the
# right child of that node.
# 
# Consider the sequence of N values reported by a preorder traversal starting
# from the root.  Call such a sequence of N values the voyage of the tree.
# 
# (Recall that a preorder traversal of a node means we report the current
# node's value, then preorder-traverse the left child, then preorder-traverse
# the right child.)
# 
# Our goal is to flip the least number of nodes in the tree so that the voyage
# of the tree matches the voyage we are given.
# 
# If we can do so, then return a list of the values of all nodes flipped.  You
# may return the answer in any order.
# 
# If we cannot do so, then return the list [-1].
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 100
# 
# 
# 
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
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # Depth-First Search
        # If at any node, the node's value doesn't match the voyage, the answer is [-1].
        # Otherwise, we know when to flip: the next number we are expecting in the voyage voyage[i] is different from the next child.
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # self.flipped = []
        # self.i = 0

        # def dfs(node):
        #     if node:
        #         if node.val != voyage[self.i]:
        #             self.flipped = [-1]
        #             return
        #         self.i += 1

        #         if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
        #             self.flipped.append(node.val)
        #             dfs(node.right)
        #             dfs(node.left)
        #         else:
        #             dfs(node.left)
        #             dfs(node.right)

        # dfs(root)
        # if self.flipped and self.flipped[0] == -1:
        #     self.flipped = [-1]
        # return self.flipped


        res = []
        self.i = 0

        def dfs(node):
            if not node: return True

            if node.val != voyage[self.i]:
                return False

            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                res.append(node.val)
                node.left, node.right = node.right, node.left

            return dfs(node.left) and dfs(node.right)

        return res if dfs(root) else [-1]
        
# @lc code=end

