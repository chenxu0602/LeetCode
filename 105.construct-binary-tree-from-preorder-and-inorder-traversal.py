#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (45.40%)
# Likes:    2551
# Dislikes: 75
# Total Accepted:    298.9K
# Total Submissions: 657K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # if inorder:
        #     idx = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[idx])
        #     root.left = self.buildTree(preorder, inorder[:idx])
        #     root.right = self.buildTree(preorder, inorder[idx+1:])
        #     return root
        # return None

        def dfs(left, right):
            nonlocal pre_idx

            if left == right:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            idx = idx_map[root_val]

            pre_idx += 1
            root.left = dfs(left, idx)
            root.right = dfs(idx+1, right)
            return root

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, len(inorder))
        
# @lc code=end

