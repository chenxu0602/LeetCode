#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (76.56%)
# Likes:    1174
# Dislikes: 145
# Total Accepted:    91.6K
# Total Submissions: 119.4K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # if not nums:
        #     return None

        # i = nums.index(max(nums))
        # node = TreeNode(nums[i])

        # node.left = self.constructMaximumBinaryTree(nums[:i])
        # node.right = self.constructMaximumBinaryTree(nums[i+1:])

        # return node


        # Time  complexity: O(n^2)
        # Space complexity: O(n)
        def calc_max(nums, l, r):
            max_i = l
            for i in range(l, r):
                if nums[max_i] < nums[i]:
                    max_i = i
            return max_i

        def construct(nums, l, r):
            if l == r: return None
            max_i = calc_max(nums, l, r)
            node = TreeNode(nums[max_i])
            node.left = construct(nums, l, max_i)
            node.right = construct(nums, max_i + 1, r)
            return node 

        return construct(nums, 0, len(nums))
        

