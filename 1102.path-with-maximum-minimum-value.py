#
# @lc app=leetcode id=1102 lang=python3
#
# [1102] Path With Maximum Minimum Value
#
# https://leetcode.com/problems/path-with-maximum-minimum-value/description/
#
# algorithms
# Medium (49.21%)
# Likes:    549
# Dislikes: 62
# Total Accepted:    23.7K
# Total Submissions: 47.6K
# Testcase Example:  '[[5,4,5],[1,2,6],[7,4,6]]'
#
# Given a matrix of integers A with R rows and C columns, find the maximum
# score of a path starting at [0,0] and ending at [R-1,C-1].
# 
# The score of a path is the minimum value in that path.  For example, the
# value of the path 8 →  4 →  5 →  9 is 4.
# 
# A path moves some number of times from one visited cell to any neighbouring
# unvisited cell in one of the 4 cardinal directions (north, east, west,
# south).
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[5,4,5],[1,2,6],[7,4,6]]
# Output: 4
# Explanation: 
# The path with the maximum score is highlighted in yellow. 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
# Output: 2
# 
# Example 3:
# 
# 
# 
# 
# Input:
# [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
# Output: 3
# 
# 
# 
# Note:
# 
# 
# 1 <= R, C <= 100
# 0 <= A[i][j] <= 10^9
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # O(MNlog(MN))
        m, n = map(len, (A, A[0]))
        pq, score, A[m - 1][n - 1] = [(-A[m - 1][n - 1], m - 1, n - 1)], A[0][0], -1

        while pq:
            s, i, j = heapq.heappop(pq)
            score = min(-s, score)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if not (x or y):
                    return score
                if 0 <= x < m and 0 <= y < n and A[x][y] >= 0:
                    heapq.heappush(pq, (-A[x][y], x, y))
                    A[x][y] = -1

        
# @lc code=end

