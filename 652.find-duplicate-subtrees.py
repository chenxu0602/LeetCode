#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (49.95%)
# Likes:    1392
# Dislikes: 209
# Total Accepted:    66.3K
# Total Submissions: 131.8K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200
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
from collections import Counter, defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # Depth-First Search
        # We visit each node once, but each creation of serial may take O(N) work.
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        count = Counter()
        ans = []
        def collect(node):
            if not node: return '#'
            serial = '{},{},{}'.format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


        # Unique Identifier
        # trees = defaultdict()
        # trees.default_factory = trees.__len__
        # count = Counter()
        # ans = []

        # def lookup(node):
        #     if node:
        #         uid = trees[node.val, lookup(node.left), lookup(node.right)]
        #         count[uid] += 1
        #         if count[uid] == 2:
        #             ans.append(node)
        #         return uid

        # lookup(root)
        # return ans
        
# @lc code=end

