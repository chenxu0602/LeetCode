#
# @lc app=leetcode id=1478 lang=python3
#
# [1478] Allocate Mailboxes
#
# https://leetcode.com/problems/allocate-mailboxes/description/
#
# algorithms
# Hard (54.97%)
# Likes:    320
# Dislikes: 4
# Total Accepted:    6K
# Total Submissions: 10.9K
# Testcase Example:  '[1,4,8,10,20]\n3'
#
# Given the array houses and an integer k. where houses[i] is the location of
# the ith house along a street, your task is to allocate k mailboxes in the
# street.
# 
# Return the minimum total distance between each house and its nearest
# mailbox.
# 
# The answer is guaranteed to fit in a 32-bit signed integer.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3|
# + |9-8| + |10-9| + |20-20| = 5 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3|
# + |5-3| + |12-14| + |18-14| = 9.
# 
# 
# Example 3:
# 
# 
# Input: houses = [7,4,6,1], k = 1
# Output: 8
# 
# 
# Example 4:
# 
# 
# Input: houses = [3,6,14,10], k = 4
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# n == houses.length
# 1 <= n <= 100
# 1 <= houses[i] <= 10^4
# 1 <= k <= n
# Array houses contain unique integers.
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # O(n^3) / O(n^2)

        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])

        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return float("inf")
            ans = float("inf")
            for j in range(i, n):
                cost = costs[i][j] # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)

        # dp = [[float("inf")] * k for _ in range(n)]
        # for i in range(n): 
        #     dp[i][0] = costs[0][i]

        # for k2 in range(1, k):
        #     for i in range(n):
        #         for j in range(i):
        #             dp[i][k2] = min(dp[i][k2], dp[j][k2 - 1] + costs[j + 1][i])

        # return dp[-1][-1]
        
# @lc code=end

