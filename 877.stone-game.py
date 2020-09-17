#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (64.62%)
# Likes:    799
# Dislikes: 1082
# Total Accepted:    65K
# Total Submissions: 99.2K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
# 
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
# 
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
# 
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
# 
# 
# Example 1:
# 
# 
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Mathematical
        # If Alex takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, she can always take the second pile. At least one of first + third, second + fourth is larger, so she can always win.
        # O(1)
        # return True


        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        # N = len(piles)

        # @lru_cache(None)
        # def dp(i, j):
        #     if i > j: return 0
        #     parity = (j - i - N) % 2
        #     if parity == 1: # first player
        #         return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
        #     else:
        #         return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        # return dp(0, N - 1) > 0


        # N = len(piles)
        # dp = [[0] * N for i in range(N)]
        # for i in range(N):
        #     dp[i][i] = piles[i]
        # for d in range(1, N):
        #     for i in range(N - d):
        #         dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

        # return dp[0][-1] > 0


        # N = len(piles)
        # dp = piles[:]
        # for d in range(1, N):
        #     for i in range(N - d):
        #         dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        # return dp[0] > 0


        N = len(piles)
        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            return max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
        return dp(0, N - 1) > 0
        
# @lc code=end

