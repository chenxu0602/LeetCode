#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (42.99%)
# Likes:    1279
# Dislikes: 27
# Total Accepted:    193K
# Total Submissions: 446.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        # if not inorder or not postorder:
        #     return None

        # root = TreeNode(postorder.pop())
        # inorderIndex = inorder.index(root.val)

        # root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        # root.left = self.buildTree(inorder[:inorderIndex], postorder)

        # return root


        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
        
# @lc code=end

