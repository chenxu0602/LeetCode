#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (72.27%)
# Likes:    547
# Dislikes: 26
# Total Accepted:    51.2K
# Total Submissions: 71.2K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level X such that the sum of all the values of nodes at
# level X is maximal.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# Example 2:
# 
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
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
from collections import defaultdict, deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # DFS : Recursive Inorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # def inorder(node, level):
        #     if node:
        #         inorder(node.left, level + 1)
        #         level_sum[level] += node.val
        #         inorder(node.right, level + 1)

        # level_sum = defaultdict(int)
        # inorder(root, 1)
        # return max(level_sum, key=level_sum.get)
        

        # BFS: Short Python Solution
        # Time  complexity: O(N)
        # Space complexity: O(N)
        curr_level = max_level = 1
        max_sum = float("-inf")
        queue = [root,]

        while queue:
            curr_sum = sum([x.val for x in queue])
            if curr_sum > max_sum:
                max_sum, max_level = curr_sum, curr_level

            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1

        return max_level

# @lc code=end

