#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.51%)
# Likes:    1498
# Dislikes: 136
# Total Accepted:    364.1K
# Total Submissions: 869.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
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
    def isBalanced(self, root: TreeNode) -> bool:

        # Top-down recursion
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) < 2 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)

        # Bottom-up recursion
        # Time  complexity: O(n)
        # Space complexity: O(n)
        def helper(node):
            if not node:
                return True, -1

            leftIsBalanced, leftHeight = helper(root.left)
            if not leftIsBalanced:
                return False, 0

            rightIsBalanced, rightHeight = helper(root.right)
            if not rightHeight:
                return False, 0

            return abs(leftHeight - rightHeight) < 2, 1 + max(leftHeight, rightHeight)

        return helper(root)[0]


        # Simpler bottom-up recursion
        def height(node):
            if node is None:
                return 0

            left, right = map(height, (node.left, node.right))

            if left == -1:
                return -1

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        return height(root) != 1
# @lc code=end

