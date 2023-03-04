#
# @lc app=leetcode id=2435 lang=python3
#
# [2435] Paths in Matrix Whose Sum Is Divisible by K
#

# @lc code=start
from collections import Counter

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m, n = map(len, (grid, grid[0]))
        MOD = 10**9 + 7

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for kk in range(k):
                    if j > 0:
                        dp[i][j][(kk + grid[i][j]) % k] += dp[i][j - 1][kk] % MOD
                    if i > 0:
                        dp[i][j][(kk + grid[i][j]) % k] += dp[i - 1][j][kk] % MOD

        return dp[-1][-1][0] % MOD

        
# @lc code=end

