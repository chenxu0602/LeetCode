#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (69.90%)
# Likes:    242
# Dislikes: 9
# Total Accepted:    10.3K
# Total Submissions: 14.9K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth first search on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  (If the depth of a node
# is D, the depth of its immediate child is D+1.  The depth of the root node is
# 0.)
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output S of this traversal, recover the tree and return its
# root.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the original tree is between 1 and 1000.
# Each node will have a value between 1 and 10^9.
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import re

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]

        def dfs(level):
            if not vals or level != vals[-1][0]:
                return None

            node = TreeNode(vals.pop()[1])
            node.left = dfs(level+1)
            node.right = dfs(level+1)
            return node

        return dfs(0)

