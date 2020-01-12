#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
#
# algorithms
# Medium (64.44%)
# Likes:    103
# Dislikes: 145
# Total Accepted:    8.7K
# Total Submissions: 13.5K
# Testcase Example:  '[1,2,3]'
#
# Given a rooted binary tree, return the lowest common ancestor of its deepest
# leaves.
# 
# Recall that:
# 
# 
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0, and if the depth of a node is d, the
# depth of each of its children is d+1.
# The lowest common ancestor of a set S of nodes is the node A with the largest
# depth such that every node in S is in the subtree with root A.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: [1,2,3]
# Explanation: 
# The deepest leaves are the nodes with values 2 and 3.
# The lowest common ancestor of these leaves is the node with value 1.
# The answer returned is a TreeNode object (not an array) with serialization
# "[1,2,3]".
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4]
# Output: [4]
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: [2,4,5]
# 
# 
# 
# Constraints:
# 
# 
# The given tree will have between 1 and 1000 nodes.
# Each node of the tree will have a distinct value between 1 and 1000.
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
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        def dfs(root):
            if not root:
                return 0, None

            h1, lca1 = dfs(root.left)
            h2, lca2 = dfs(root.right)

            if h1 > h2:
                return h1 + 1, lca1

            if h1 < h2:
                return h2 + 1, lca2

            return h1 + 1, root

        return dfs(root)[1]
        """

        self.lca, self.deepest = None, 0
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        dfs(root, 0)
        return self.lca
        
# @lc code=end

