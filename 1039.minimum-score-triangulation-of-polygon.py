#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/
#
# algorithms
# Medium (48.90%)
# Likes:    511
# Dislikes: 62
# Total Accepted:    11.7K
# Total Submissions: 23.6K
# Testcase Example:  '[1,2,3]'
#
# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i],
# ..., A[N-1] in clockwise order.
# 
# Suppose you triangulate the polygon into N-2 triangles.  For each triangle,
# the value of that triangle is the product of the labels of the vertices, and
# the total score of the triangulation is the sum of these values over all N-2
# triangles in the triangulation.
# 
# Return the smallest possible total score that you can achieve with some
# triangulation of the polygon.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: 6
# Explanation: The polygon is already triangulated, and the score of the only
# triangle is 6.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 +
# 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5
# + 1*1*1 = 13.
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 50
# 1 <= A[i] <= 100
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # If we pick a side of our polygon, it can form n - 2 triangles. Each such triangle forms 2 sub-polygons. We can analyze n - 2 triangles, and get the minimum score for sub-polygons using the recursion.

        # n = len(A)
        # dp = [[0] * n for _ in range(n)]
        # for d in range(2, n):
        #     for i in range(n - d):
        #         j = i + d
        #         dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in range(i + 1, j))
        # return dp[0][n - 1]


        @lru_cache(None)
        def dp(i, j):
            return min([dp(i, k) + dp(k, j) + A[i] * A[k] * A[j] for k in range(i + 1, j)] or [0])
        return dp(0, len(A) - 1)
        
# @lc code=end

