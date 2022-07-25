#
# @lc app=leetcode id=2327 lang=python3
#
# [2327] Number of People Aware of a Secret
#

# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # dp = [1] + [0] * (n - 1)
        # MOD = 10**9 + 7
        # share = 0
        # for i in range(1, n):
        #     dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % MOD
        # return sum(dp[-forget:]) % MOD

        dp = [1] + [0] * forget
        MOD = 10**9 + 7
        share = 0
        for i in range(1, n):
            dp[i % forget] = share = (share + dp[(i - delay) % forget] - dp[i % forget]) % MOD
        return sum(dp) % MOD
        
# @lc code=end

