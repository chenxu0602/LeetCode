#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (37.89%)
# Likes:    928
# Dislikes: 61
# Total Accepted:    131.9K
# Total Submissions: 348K
# Testcase Example:  '[2,1,3]\n1'
#
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
# 
# The successor of a node p is the node with the smallest key greater than
# p.val.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the
# return value is of TreeNode type.
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the
# answer is null.
# 
# 
# 
# 
# Note:
# 
# 
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
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
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # Time  complexity: O(H_p) in the best case, when node p has a right child. O(H) in the worst case of no right child.
        # Space complexity: O(1) in the best case when node p has a right child. Otherwise, up to O(H) to keep the stack.
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        # if p.right:
        #     p = p.right
        #     while p.left:
        #         p = p.left
        #     return p

        # # the successor is somewhere upper in the tree
        # stack, inorder = [], float("-inf")

        # # inorder traversal : left -> node -> right
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     if inorder == p.val:  # if the previous node was equal to p
        #         return root       # then the current node is its 

        #     inorder = root.val
        #     root = root.right
        
        # return None




        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right

        return succ
# @lc code=end

