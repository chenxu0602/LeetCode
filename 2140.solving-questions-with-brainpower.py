#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
from functools import lru_cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        """
        @lru_cache(None)
        def dp(i):
            if i >= len(questions):
                return 0

            points, jump = questions[i][0], questions[i][1]
            return max(dp(i + 1), points + dp(i + jump + 1))

        return dp(0)
        """

        dp = [0] * (len(questions) + 1)
        for i in range(len(questions) - 1, -1, -1):
            points, jump = questions[i][0], questions[i][1]
            dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])

        return dp[0]

        
# @lc code=end

