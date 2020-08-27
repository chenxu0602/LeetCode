#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (46.04%)
# Likes:    3976
# Dislikes: 303
# Total Accepted:    216.9K
# Total Submissions: 459K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Prefix Sum
        # Time  complexity: O(N)
        # Space complexity: O(N)
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return

            # current prefix sum
            curr_sum += node.val

            # here is the sum we're looking for
            if curr_sum == k:
                count += 1

            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += h[curr_sum - k]

            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1

            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum)

            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            h[curr_sum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count
        
# @lc code=end

