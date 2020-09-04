#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (52.51%)
# Likes:    739
# Dislikes: 211
# Total Accepted:    66.5K
# Total Submissions: 126.2K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
# This question is the same as 530:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def minDiffInBST(self, root: TreeNode) -> int:
        # Inorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def dfs(node):
        #     return dfs(node.left) + [node.val] + dfs(node.right) if node else []

        # vals = dfs(root)
        # return min(vals[i + 1] - vals[i] for i in range(len(vals) - 1))


        # Inorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # def dfs(node):
        #     if node:
        #         dfs(node.left)
        #         self.ans = min(self.ans, node.val - self.prev)
        #         self.prev = node.val
        #         dfs(node.right)

        # self.prev, self.ans = float("-inf"), float("inf")
        # dfs(root)
        # return self.ans
        

        def dfs(node, lo, hi):
            if not node: return hi - lo
            left, right = map(dfs, (node.left, node.right), (lo, node.val), (node.val, hi))
            return min(left, right)
        return dfs(root, float("-inf"), float("inf"))
# @lc code=end

