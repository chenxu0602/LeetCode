#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (42.76%)
# Likes:    1261
# Dislikes: 72
# Total Accepted:    262.4K
# Total Submissions: 601.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        def addLevel(root, level, res):
            if root:
                if len(res) == level:
                    res.append([])

                if level % 2:
                    res[level].insert(0, root.val)
                else:
                    res[level].append(root.val)

                addLevel(root.left, level + 1, res)
                addLevel(root.right, level + 1, res)

        res = []
        addLevel(root, 0, res)
        return res
        
# @lc code=end

