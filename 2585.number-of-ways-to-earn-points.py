#
# @lc app=leetcode id=2585 lang=python3
#
# [2585] Number of Ways to Earn Points
#

# @lc code=start
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:

        # A Knapsack Problem
        # Note that dp[big] depends on dp[small],
        # if you change dp[small]first, we need to update dp[big] from old dp[small].
        # So here I iterative from dp[big] to dp[small].
        dp = [1] + [0] * target
        MOD = 10 ** 9 + 7
        for c, m in types:
            for i in range(target, -1, -1):
                for k in range(1, min(c, i // m) + 1):
                    dp[i] = (dp[i] + dp[i - m * k]) % MOD

        return dp[-1]
        
# @lc code=end

