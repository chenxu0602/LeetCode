#
# @lc app=leetcode id=2188 lang=python3
#
# [2188] Minimum Time to Finish the Race
#

# @lc code=start
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # dp[x] := the minimum time to finish x laps
        # base case: dp[1] = min(f_i) among all tires
        # transition: dp[x] = min(dp[j] + changeTime + dp[x-j]) among all possible js

        n = len(tires)
        without_change = [[float('inf')] * 20 for _ in range(n)] # the total time to run j laps consecutively with tire i

        for i in range(n):
            without_change[i][1] = tires[i][0]
            for j in range(2, 20):
                without_change[i][j] = without_change[i][j - 1] * tires[i][1]

            for j in range(2, 20):
                without_change[i][j] += without_change[i][j - 1]

        dp = [float("inf")] * (numLaps + 1)
        for i in range(n): dp[1] = min(dp[1], tires[i][0])

        for x in range(1, numLaps + 1):
            if x < 20:
                for i in range(n):
                    dp[x] = min(dp[x], without_change[i][x])

            for j in range(x - 1, max(x - 18, 1) - 1, -1):
                dp[x] = min(dp[x], dp[j] + changeTime + dp[x - j])


        return dp[numLaps]


        
# @lc code=end

