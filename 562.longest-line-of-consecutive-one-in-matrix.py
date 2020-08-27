#
# @lc app=leetcode id=562 lang=python3
#
# [562] Longest Line of Consecutive One in Matrix
#
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (45.83%)
# Likes:    334
# Dislikes: 71
# Total Accepted:    27K
# Total Submissions: 59K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,1]]'
#
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
# 
# Example:
# 
# Input:
# [[0,1,1,0],
# ⁠[0,1,1,0],
# ⁠[0,0,0,1]]
# Output: 3
# 
# 
# 
# 
# Hint:
# The number of elements in the given matrix will not exceed 10,000.
# 
#

# @lc code=start
from itertools import groupby
from collections import defaultdict

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # O(mn)
        if not M: return 0

        def score(line):
            return max(len(list(v)) if k else 0 for k, v in groupby(line))

        groups = defaultdict(list)
        for r, row in enumerate(M):
            for c, val in enumerate(row):
                groups[0, r] += val,
                groups[1, c] += val,
                groups[2, r + c] += val,
                groups[3, r - c] += val,

        return max(map(score, groups.values()))
        
# @lc code=end

