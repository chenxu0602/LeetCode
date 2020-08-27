#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (57.77%)
# Likes:    655
# Dislikes: 124
# Total Accepted:    72.3K
# Total Submissions: 124.7K
# Testcase Example:  '[5,2,-3]'
#
# 
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
# 
# 
# Examples 1
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
# 
# 
# Examples 2
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# return [2], since 2 happens twice, however -5 only occur once.
# 
# 
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        # O(N)
        def dfs(node):
            if not node: return 0
            left, right = map(dfs, (node.left, node.right))
            s = node.val + left + right
            count[s] += 1
            return s

        if not root: return []

        count = Counter()
        dfs(root)
        most_common = count.most_common()[0][1]

        return [k for k, v in count.items() if v == most_common]


        
# @lc code=end

