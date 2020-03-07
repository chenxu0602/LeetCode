#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (74.99%)
# Likes:    535
# Dislikes: 20
# Total Accepted:    36.2K
# Total Submissions: 48.2K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        # root = TreeNode(preorder[0])
        # stack = [root,]
        # for val in preorder[1:]:
        #     if val < stack[-1].val:
        #         stack[-1].left = TreeNode(val)
        #         stack.append(stack[-1].left)
        #     else:
        #         while stack and stack[-1].val < val:
        #             last = stack.pop()
        #         last.right = TreeNode(val)
        #         stack.append(last.right)
        # return root

        def dfs(lower=float("-inf"), upper=float("inf")):
            nonlocal idx
            if idx == n: return None

            val = preorder[idx]
            if val < lower or val > upper:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = dfs(lower, val)
            root.right = dfs(val, upper) 
            return root

        idx, n = 0, len(preorder)
        return dfs()
        
# @lc code=end

