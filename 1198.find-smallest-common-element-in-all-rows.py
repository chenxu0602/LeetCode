#
# @lc app=leetcode id=1198 lang=python3
#
# [1198] Find Smallest Common Element in All Rows
#
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/description/
#
# algorithms
# Medium (74.17%)
# Likes:    71
# Dislikes: 7
# Total Accepted:    6.1K
# Total Submissions: 8.2K
# Testcase Example:  '[[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]'
#
# Given a matrix mat where every row is sorted in increasing order, return the
# smallest common element in all rows.
# 
# If there is no common element, return -1.
# 
# 
# 
# Example 1:
# Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= mat.length, mat[i].length <= 500
# 1 <= mat[i][j] <= 10^4
# mat[i] is sorted in increasing order.
# 
# 
#

# @lc code=start

from collections import Counter
from functools import reduce

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        # c = Counter()
        # for row in mat:
        #     for a in row:
        #         c[a] += 1
        #         if c[a] == len(mat):
        #             return a
        # return -1

        return min(reduce(lambda x, y: set(x) & set(y), mat), default=-1)
        
# @lc code=end

