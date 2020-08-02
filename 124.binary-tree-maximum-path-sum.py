#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (32.17%)
# Likes:    2540
# Dislikes: 205
# Total Accepted:    269.6K
# Total Submissions: 837.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:

        def maxsums(node):
            if not node:
                return [-2**31] * 2

            left, right = map(maxsums, (node.left, node.right))
            return [node.val + max(left[0], right[0], 0),
                max(left + right + [node.val + left[0] + right[0]])]

        return max(maxsums(root))


        # Time  complexity: O(N)
        # Space complexity: O(H=logN)
        # def max_gain(node):
        #     nonlocal max_sum
        #     if not node:
        #         return 0

        #     # max sum on the left and right sub-trees of node
        #     left_gain, right_gain = map(max, map(max_gain, (node.left, node.right)), (0, 0))

        #     # the price to start a new path where `node` is a highest node
        #     price_newpath = node.val + left_gain + right_gain

        #     # update max_sum if it's better to start a new path
        #     max_sum = max(max_sum, price_newpath)

        #     # for recursion: return the max gain if continue the same path
        #     return node.val + max(left_gain, right_gain)

        # max_sum = float("-inf")
        # max_gain(root)
        # return max_sum

        
# @lc code=end

