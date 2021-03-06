#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (42.02%)
# Likes:    1474
# Dislikes: 26
# Total Accepted:    120.9K
# Total Submissions: 287.5K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # O(mn)
        # def dfs(matrix, x, y, dp):
        #     if dp[x][y] != 0:
        #         return dp[x][y]

        #     for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
        #             dp[x][y] = max(dp[x][y], dfs(matrix, nx, ny, dp))

        #     dp[x][y] += 1
        #     return dp[x][y]

        # if not matrix: return 0
        # m, n = map(len, (matrix, matrix[0]))

        # dp = [[0] * n for _ in range(m)]

        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         ans = max(ans, dfs(matrix, i, j, dp))

        # return ans
            



        @lru_cache(None)
        def dfs(i, j):
            val = matrix[i][j]
            return 1 + max(
                dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                dfs(i+1, j) if i < m - 1 and val > matrix[i+1][j] else 0,
                dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                dfs(i, j+1) if j < n - 1 and val > matrix[i][j+1] else 0
            )

        if not matrix: return 0
        m, n = map(len, (matrix, matrix[0]))
        return max(dfs(x, y) for x in range(m) for y in range(n))


        # matrix = {i + j*1j: val for i, row in enumerate(matrix) for j, val in enumerate(row)}
        # length = {}
        # for z in sorted(matrix, key=matrix.get):
        #     length[z] = 1 + max([length[Z] for Z in (z-1, z+1, z-1j, z+1j)
        #         if Z in matrix and matrix[z] > matrix[Z]] or [0])
        # return max(length.values(), default=0)

        # @lru_cache(None)
        # def length(z):
        #     return 1 + max([length(Z) for Z in (z-1, z+1, z-1j, z+1j)
        #         if Z in matrix and matrix[z]> matrix[Z]] or [0])
        # matrix = {i + j * 1j: val for i, row in enumerate(matrix) for j, val in enumerate(row)}
        # return max(map(length, matrix), default=0)
        
# @lc code=end

