#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (57.02%)
# Likes:    446
# Dislikes: 135
# Total Accepted:    23.3K
# Total Submissions: 40.4K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given a binary tree rooted at root, the depth of each node is the shortest
# distance to the root.
# 
# A node is deepest if it has the largest depth possible among any node in the
# entire tree.
# 
# The subtree of a node is that node, plus the set of all descendants of that
# node.
# 
# Return the node with the largest depth such that it contains all the deepest
# nodes in its subtree.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
# 
# 
# 
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the
# given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node
# with value 2.
# Both the input and output have TreeNode type.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import namedtuple

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        """
        depth = {None: -1}

        def dfs(node, par=None):
            if node:
                depth[node] = depth[par] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        max_depth = max(depth.values())

        def answer(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)
        """

        result = namedtuple("result", ("node", "dist"))

        def dfs(node):
            if not node:
                return result(None, 0)

            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist:
                return result(L.node, L.dist + 1)
            if L.dist < R.dist:
                return result(R.node, R.dist + 1)
            return result(node, L.dist + 1)

        return dfs(root).node

        

