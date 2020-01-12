#
# @lc app=leetcode id=562 lang=python3
#
# [562] Longest Line of Consecutive One in Matrix
#
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (43.95%)
# Likes:    208
# Dislikes: 57
# Total Accepted:    17.3K
# Total Submissions: 39.2K
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
import itertools
from collections import defaultdict

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """
        def score(line):
            ans = count = 0
            for x in line:
                if x:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
            return count
        """

        if not M: return 0

        def score(line):
            return max(len(list(v)) if k else 0 for k, v in itertools.groupby(line))

        groups = defaultdict(list)
        for r, row in enumerate(M):
            for c, val in enumerate(row):
                groups[0, r] += [val]
                groups[1, c] += [val]
                groups[2, r+c] += [val]
                groups[3, r-c] += [val]

        return max(map(score, groups.values()))
                

        

