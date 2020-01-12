#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (43.11%)
# Likes:    1946
# Dislikes: 90
# Total Accepted:    111K
# Total Submissions: 257.4K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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
    def dfs(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t - node.val:
                hit += 1
        targets = [t - node.val for t in targets] + [origin]
        return hit + self.dfs(node.left, origin, targets) + self.dfs(node.right, origin, targets)

    def pathSum(self, root: TreeNode, sum: int) -> int:

        
        return self.dfs(root, sum, [sum]) 

        """
        def helper(t, s):
            if not t: return 0
            return int(t.val == s) + helper(t.left, s-t.val) + helper(t.right, s-t.val)

        if not root: return 0
        res = int(root.val == sum)
        res = res + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        res = res + helper(root.left, sum-root.val) + helper(root.right, sum-root.val)

        return res
        """

