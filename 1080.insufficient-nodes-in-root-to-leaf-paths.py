#
# @lc app=leetcode id=1080 lang=python3
#
# [1080] Insufficient Nodes in Root to Leaf Paths
#
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/description/
#
# algorithms
# Medium (49.25%)
# Likes:    195
# Dislikes: 360
# Total Accepted:    15.1K
# Total Submissions: 30.4K
# Testcase Example:  '[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1'
#
# Given the root of a binary tree, consider all root to leaf paths: paths from
# the root to any leaf.  (A leaf is a node with no children.)
# 
# A node is insufficient if every such root to leaf path intersecting this node
# has sum strictly less than limit.
# 
# Delete all insufficient nodes simultaneously, and return the root of the
# resulting binary tree.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 
# Output: [1,2,3,4,null,null,7,8,9,null,14]
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 
# Output: [5,4,8,11,null,17,4,7,null,null,null,5]
# 
# 
# 
# Example 3:
# 
# 
# 
# Input: root = [1,2,-3,-5,null,4,null], limit = -1
# 
# Output: [1,null,-3,4]
# 
# 
# 
# 
# Note:
# 
# 
# The given tree will have between 1 and 5000 nodes.
# -10^5 <= node.val <= 10^5
# -10^9 <= limit <= 10^9
# 
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
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        if root.left is root.right:
            return None if root.val < limit else root

        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)

        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)

        return root if root.left or root.right else None

        
        
# @lc code=end

