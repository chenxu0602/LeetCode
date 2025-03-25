#
# @lc app=leetcode id=3332 lang=python3
#
# [3332] Maximum Points Tourist Can Earn
#

# @lc code=start
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        dp = [[0] * n for _ in range(k + 1)]

        for j in range(n):
            dp[1][j] = stayScore[0][j]
            for i in range(n):
                dp[1][j] = max(dp[1][j], travelScore[i][j])

        for i in range(2, k + 1):
            for j in range(n):
                for k in range(n):
                    if k == j:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j] + stayScore[i - 1][j])
                    else:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + travelScore[k][j])

        return max(dp[-1])

        
# @lc code=end

