#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/
#
# algorithms
# Medium (31.88%)
# Likes:    252
# Dislikes: 15
# Total Accepted:    9K
# Total Submissions: 28.1K
# Testcase Example:  '[[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]'
#
# You are given a rows x cols matrix grid. Initially, you are located at the
# top-left corner (0, 0), and in each step, you can only move right or down in
# the matrix.
# 
# Among all possible paths starting from the top-left corner (0, 0) and ending
# in the bottom-right corner (rows - 1, cols - 1), find the path with the
# maximum non-negative product. The product of a path is the product of all
# integers in the grid cells visited along the path.
# 
# Return the maximum non-negative product modulo 10^9 + 7. If the maximum
# product is negative return -1.
# 
# Notice that the modulo is performed after getting the maximum product.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[-1,-2,-3],
# [-2,-3,-3],
# [-3,-3,-2]]
# Output: -1
# Explanation: It's not possible to get non-negative product in the path from
# (0, 0) to (2, 2), so return -1.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,-2,1],
# [1,-2,1],
# [3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 =
# 8).
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1, 3],
# [0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
# 
# 
# Example 4:
# 
# 
# Input: grid = [[ 1, 4,4,0],
# [-2, 0,0,1],
# [ 1,-1,1,1]]
# Output: 2
# Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1
# = 2).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= rows, cols <= 15
# -4 <= grid[i][j] <= 4
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # MOD = 10**9 + 7
        # m, n = map(len, (grid, grid[0]))

        # @lru_cache(None)
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return float("-inf"), float("inf")
        #     if i == 0 and j == 0:
        #         return grid[0][0], grid[0][0]
        #     if grid[i][j] == 0:
        #         return 0, 0

        #     mx1, mn1 = dfs(i - 1, j)
        #     mx2, mn2 = dfs(i, j - 1)
        #     mx, mn = max(mx1, mx2) * grid[i][j], min(mn1, mn2) * grid[i][j]
        #     return (mx, mn) if grid[i][j] > 0 else (mn, mx)

        # mx, _ = dfs(m - 1, n - 1)
        # return -1 if mx < 0 else mx % MOD


        MOD = 10**9 + 7
        m, n = map(len, (grid, grid[0]))
        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]
        mx[0][0] = mn[0][0] = grid[0][0]

        for i in range(1, m):
            mn[i][0] = mx[i][0] = mx[i - 1][0] * grid[i][0]

        for j in range(1, n):
            mn[0][j] = mx[0][j] = mx[0][j - 1] * grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] < 0:
                    mx[i][j] = min(mn[i - 1][j], mn[i][j - 1]) * grid[i][j]
                    mn[i][j] = max(mx[i - 1][j], mx[i][j - 1]) * grid[i][j]
                else:
                    mx[i][j] = max(mx[i - 1][j], mx[i][j - 1]) * grid[i][j]
                    mn[i][j] = min(mn[i - 1][j], mn[i][j - 1]) * grid[i][j]

        ans = mx[m - 1][n - 1]
        return -1 if not ans >= 0 else ans % MOD
        
# @lc code=end

