#
# @lc app=leetcode id=3336 lang=python3
#
# [3336] Find the Number of Subsequences With Equal GCD
#

# @lc code=start
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        n = max(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for a in nums:
            dp2 = [[0] * (n + 1) for _ in range(n + 1)]
            for i in range(n, -1, -1):
                for j in range(n, -1, -1):
                    i2 = gcd(i, a)
                    j2 = gcd(j, a)
                    dp2[i2][j] = (dp2[i2][j] + dp[i][j]) % MOD
                    dp2[i][j2] = (dp2[i][j2] + dp[i][j]) % MOD
                    dp2[i][j] = (dp2[i][j] + dp[i][j]) % MOD
            dp = dp2

        return sum(dp[i][i] for i in range(1, n + 1)) % MOD
        
# @lc code=end

