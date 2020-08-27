#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (55.17%)
# Likes:    1997
# Dislikes: 119
# Total Accepted:    123.4K
# Total Submissions: 222.5K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# Example:
# 
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        # Recursion
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # if root is not None:
        #     self.convertBST(root.right)
        #     self.total += root.val
        #     root.val = self.total
        #     self.convertBST(root.left)
        # return root


        # Iteration with a Stack 
        # Time  complexity: O(n)
        # Space complexity: O(n)
        total = 0
        node, stack = root, []

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left

        return root


        
# @lc code=end

