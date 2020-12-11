#
# @lc app=leetcode id=1676 lang=python3
#
# [1676] Lowest Common Ancestor of a Binary Tree IV
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/
#
# algorithms
# Medium (75.82%)
# Likes:    30
# Dislikes: 1
# Total Accepted:    993
# Total Submissions: 1.3K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n[4,7]'
#
# Given the root of a binary tree and an array of TreeNode objects nodes,
# return the lowest common ancestor (LCA) of all the nodes in nodes. All the
# nodes will exist in the tree, and all values of the tree's nodes are unique.
# 
# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of
# n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every
# pi as a descendant (where we allow a node to be a descendant of itself) for
# every valid i". A descendant of a node x is a node y that is on the path from
# node x to some leaf node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
# Output: 1
# Explanation: The lowest common ancestor of a single node is the node
# itself.
# 
# 
# 
# Example 3:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
# Output: 5
# Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node
# 5.
# 
# 
# Example 4:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [0,1,2,3,4,5,6,7,8]
# Output: 3
# Explanation: The lowest common ancestor of all the nodes is the root
# node.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# All nodes[i] will exist in the tree.
# All nodes[i] are distinct.
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
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Time  complexity: O(N)
        # Space complexity: O(H + len(nodes))
        def dfs(node):
            if not node:
                return None
            if node in nodes:
                return node

            left, right = map(dfs, (node.left, node.right))
            if left and right:
                return node

            return left or right

        return dfs(root)
        
# @lc code=end

