#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (34.90%)
# Likes:    558
# Dislikes: 135
# Total Accepted:    29.3K
# Total Submissions: 83.3K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # Time  complexity: O(mnN)
        # Space complexity: O(mnN)
        # @lru_cache(None)
        # def dfs(m, n, N, i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return 1
        #     if N == 0:
        #         return 0

        #     path = dfs(m, n, N - 1, i - 1, j) + dfs(m, n, N - 1, i + 1, j) \
        #         + dfs(m, n, N - 1, i, j - 1) + dfs(m, n, N - 1, i, j + 1)

        #     return path % (10**9 + 7)

        # return dfs(m, n, N, i, j)
        


        # Time  complexity: O(mnN)
        # Space complexity: O(mn)
        M = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        count = 0

        for move in range(1, N + 1):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if i == m - 1:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    if j == n - 1:
                        count = (count + dp[i][j]) % M

                    temp[i][j] += dp[i-1][j] if i > 0 else 0
                    temp[i][j] += dp[i+1][j] if i < m - 1 else 0
                    temp[i][j] += dp[i][j-1] if j > 0 else 0
                    temp[i][j] += dp[i][j+1] if j < n - 1 else 0

            dp = temp

        return count
# @lc code=end

