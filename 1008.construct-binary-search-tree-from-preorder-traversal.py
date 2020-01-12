#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (73.25%)
# Likes:    367
# Dislikes: 14
# Total Accepted:    24.8K
# Total Submissions: 33.6K
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
        """

        """
        def helper(in_left=0, in_right=len(preorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            index = idx_map[root_val]

            pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index+1, in_right)
            return root

        inorder = sorted(preorder)
        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()
        """

        """
        def helper(lower=float("-inf"), upper=float("inf")):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]
            if val < lower or val > upper:
                return None
            
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()
        """

        n = len(preorder)
        if not n:
            return None

        root = TreeNode(preorder[0])
        stack = [root, ]

        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])

            while stack and stack[-1].val < child.val:
                node = stack.pop()

            if node.val < child.val:
                node.right = child
            else:
                node.left = child

            stack.append(child)
        return root

            
        

