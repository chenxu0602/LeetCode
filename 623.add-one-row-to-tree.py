#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (47.50%)
# Likes:    301
# Dislikes: 109
# Total Accepted:    28K
# Total Submissions: 58.7K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree, then value v and depth d, you need to add a
# row of nodes with value v at the given depth d. The root node is at depth
# 1. 
# 
# The adding rule is: given a positive integer depth d, for each NOT null tree
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree
# root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be
# the right subtree of the new right subtree root. If depth d is 1 that means
# there is no depth d-1 at all, then create a tree node with value v as the new
# root of the whole original tree, and the original tree is the new root's left
# subtree.
# 
# Example 1:
# 
# Input: 
# A binary tree as following:
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
# ⁠      4
# ⁠     / \
# ⁠    1   1
# ⁠   /     \
# ⁠  2       6
# ⁠ / \     / 
# ⁠3   1   5   
# 
# 
# 
# 
# 
# Example 2:
# 
# Input: 
# A binary tree as following:
# ⁠     4
# ⁠    /   
# ⁠   2    
# ⁠  / \   
# ⁠ 3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
# ⁠     4
# ⁠    /   
# ⁠   2
# ⁠  / \    
# ⁠ 1   1
# ⁠/     \  
# 3       1
# 
# 
# 
# Note:
# 
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            nodeNew = TreeNode(v)
            nodeNew.left = root
            return nodeNew

        if not root:
            return None

        if d == 2:
            l, r = root.left, root.right
            root.left, root.right = TreeNode(v), TreeNode(v)
            root.left.left, root.right.right = l, r
            return root

        root.left = self.addOneRow(root.left, v, d-1)
        root.right = self.addOneRow(root.right, v, d-1)
        return root
        

