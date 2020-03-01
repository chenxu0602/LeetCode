#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (46.13%)
# Likes:    2128
# Dislikes: 273
# Total Accepted:    297.2K
# Total Submissions: 643.4K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # if not root: return None
        # self.flatten(root.right)
        # self.flatten(root.left)

        # root.right = self.prev
        # root.left = None
        # self.prev = root

        last = TreeNode(-1)
        stack = [root,]

        while stack:
            node = stack.pop()
            last.right = node
            last.left = None

            if node and node.right:
                stack.append(node.right)

            if node and node.left:
                stack.append(node.left)

            last = node

        
# @lc code=end

