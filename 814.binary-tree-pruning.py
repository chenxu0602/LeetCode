#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (71.68%)
# Likes:    637
# Dislikes: 21
# Total Accepted:    40.3K
# Total Submissions: 56.3K
# Testcase Example:  '[1,null,0,0,1]'
#
# We are given the head node root of a binary tree, where additionally every
# node's value is either a 0 or a 1.
# 
# Return the same tree where every subtree (of the given tree) not containing a
# 1 has been removed.
# 
# (Recall that the subtree of a node X is X, plus every node that is a
# descendant of X.)
# 
# 
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
# ⁠
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# 
# 
# 
# 
# 
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# 
# 
# 
# 
# 
# 
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# The binary tree will have at most 100 nodes.
# The value of each node will only be 0 or 1.
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
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None

        """
        if root is None: return None
        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)

        if not l: root.left = None
        if not r: root.right = None

        if root.val == 1 or l or r:
            return root
        else:
            return None
        """
        

