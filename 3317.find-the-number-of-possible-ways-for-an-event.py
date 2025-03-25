#
# @lc app=leetcode id=3317 lang=python3
#
# [3317] Find the Number of Possible Ways for an Event
#

# @lc code=start
from math import comb

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:

        MOD = 10**9 + 7
        dp = [[0] * 1001 for _ in range(1001)]
        dp[0][0] = 1
        for i in range(1, 1001):
            for j in range(1, n + 1):
                dp[i][j] = j * (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

        return sum(comb(x, st) * pow(y, st, MOD) * dp[n][st] for st in range(1, min(n + 1, x + 1))) % MOD
        

        
# @lc code=end

