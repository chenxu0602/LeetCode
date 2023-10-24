#
# @lc app=leetcode id=2787 lang=python3
#
# [2787] Ways to Express an Integer as Sum of Powers
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        # MOD = 10**9 + 7
        # @lru_cache(None)
        # def dfs(n, x, m):
        #     r = n - m ** x
        #     if r == 0: return 1
        #     elif r > 0:
        #         return dfs(n, x, m + 1) + dfs(r, x, m + 1)
        #     else:
        #         return 0

        # return dfs(n, x, 1) % MOD


        dp = [0] * (n + 1)
        MOD = 10 ** 9 + 7

        dp[0] = 1

        for j in range(1, n + 1):
            m = j ** x
            for i in range(n, 0, -1):
                if i - m >= 0:
                    dp[i] += dp[i - m] 
                    dp[i] %= MOD

        return dp[n] % MOD

        
# @lc code=end

