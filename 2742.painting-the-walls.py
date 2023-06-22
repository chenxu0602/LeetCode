#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#

# @lc code=start
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        n = len(cost)
        dp = [0] + [float("inf")] * n

        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)

        return dp[n]
        
# @lc code=end

