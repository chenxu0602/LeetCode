#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (41.90%)
# Likes:    1264
# Dislikes: 47
# Total Accepted:    108K
# Total Submissions: 257.5K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from hashlib import sha256

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # O(s x t)
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


        # Mkerle hashing
        # O(s + t)
        # def hash_(x):
        #     S = sha256()
        #     S.update(x.encode('utf-8'))
        #     return S.hexdigest()

        # def merkle(node):
        #     if not node: return '#'
        #     left, right = map(merkle, (node.left, node.right))
        #     node.merkle = hash_(left + str(node.val) + right)
        #     return node.merkle

        # def dfs(node):
        #     if not node: return False
        #     return node.merkle == t.merkle or dfs(node.left) or dfs(node.right)

        # merkle(s); merkle(t)
        # dfs(s)
        


        

