#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#

# @lc code=start
from collections import Counter

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        # dp[i] = dp[i - zero] + dp[i - one]
        dp = Counter({0: 1})
        MOD = 10**9 + 7
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % MOD

        return sum(dp[i] for i in range(low, high + 1)) % MOD
        
# @lc code=end

