#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (47.81%)
# Likes:    876
# Dislikes: 164
# Total Accepted:    254.4K
# Total Submissions: 523.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def dfs(root, level, res):
            if root:
                if len(res) == level:
                    res.append([])
                res[level].append(root.val)
                dfs(root.left, level+1, res)
                dfs(root.right, level+1, res)

        res = []
        dfs(root, 0, res)
        return res[::-1]

        """
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))

        return res[::-1]
        """

                
        
# @lc code=end

