#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (53.33%)
# Likes:    1528
# Dislikes: 215
# Total Accepted:    357.8K
# Total Submissions: 669.8K
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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        # levels = []
        # if not root:
        #     return levels

        # def helper(node, level):
        #     if len(levels) == level:
        #         levels.append([])

        #     levels[level].append(node.val)

        #     if node.left:
        #         helper(node.left, level + 1)
        #     if node.right:
        #         helper(node.right, level + 1)

        # helper(root, 0)
        # return levels[::-1]

        levels = []
        next_level = deque([root])

        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])

            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return levels[::-1]

        
# @lc code=end

