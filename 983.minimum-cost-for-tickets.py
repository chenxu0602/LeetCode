#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (57.53%)
# Likes:    676
# Dislikes: 15
# Total Accepted:    22.6K
# Total Submissions: 39.2K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# In a country popular for train travel, you have planned some train travelling
# one year in advance.  The days of the year that you will travel is given as
# an array days.  Each day is an integer from 1 to 365.
# 
# Train tickets are sold in 3 different ways:
# 
# 
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# 
# 
# The passes allow that many days of consecutive travel.  For example, if we
# get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6,
# 7, and 8.
# 
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
# 
# 
# 
# Example 1:
# 
# 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# 
# 
# 
# Example 2:
# 
# 
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Dynamic Programming (Day Variant)
        # Time  complexity: O(W), where W = 365
        # Space complexity: O(W)
        # dayset = set(days)
        # durations = [1, 7, 30]

        # @lru_cache(None)
        # def dp(i):
        #     if i > 365:
        #         return 0
        #     elif i in dayset:
        #         return min(dp(i + d) + c for c, d in zip(costs, durations))
        #     else:
        #         return dp(i + 1)

        # return dp(1)


        # Dynamic Programming (Window Variant)
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N = len(days)
        # durations = [1, 7, 30]

        # @lru_cache(None)
        # def dp(i): # How much money to do days[i]+
        #     if i >= N: return 0

        #     ans = float("inf")
        #     j = i
        #     for c, d in zip(costs, durations):
        #         while j < N and days[j] < days[i] + d:
        #             j += 1
        #         ans = min(ans, dp(j) + c)

        #     return ans

        # return dp(0)


        # n, plans, days = max(days) + 1, [1, 7, 30], set(days)
        # dp = [0] * n
        # for i in range(1, n):
        #     dp[i] = min((dp[max(0, i - p)] + c for p, c in zip(plans, costs))) if i in days else dp[i - 1]
        # return dp[-1]

        dp, prev, plans = [0] * (max(days) + 1), 0, [1, 7, 30]
        for curr in days:
            dp[prev:curr] = [dp[prev]] * (curr - prev)
            dp[curr], prev = min(dp[max(curr - p, 0)] + c for p, c in zip(plans, costs)), curr
        return dp[-1]



