#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (47.94%)
# Likes:    1613
# Dislikes: 94
# Total Accepted:    357.3K
# Total Submissions: 744.7K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursive Approach
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # parent_val = root.val
        # p_val = p.val
        # q_val = q.val

        # if p_val > parent_val and q_val > parent_val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif p_val < parent_val and q_val < parent_val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root


        # Iterative Approach
        # Time  complexity: O(N)
        # Space complexity: O(1)
        p_val = p.val
        q_val = q.val

        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
        
# @lc code=end

