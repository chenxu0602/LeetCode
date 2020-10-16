#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
# https://leetcode.com/problems/stone-game-ii/description/
#
# algorithms
# Medium (63.13%)
# Likes:    576
# Dislikes: 141
# Total Accepted:    19.6K
# Total Submissions: 30.3K
# Testcase Example:  '[2,7,9,4,4]'
#
# Alex and Lee continue their games with piles of stones.  There are a number
# of piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].  The objective of the game is to end with the most stones. 
# 
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# 
# On each player's turn, that player can take all the stones in the first X
# remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# 
# The game continues until all the stones have been taken.
# 
# Assuming Alex and Lee play optimally, return the maximum number of stones
# Alex can get.
# 
# 
# Example 1:
# 
# 
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles,
# then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If
# Alex takes two piles at the beginning, then Lee can take all three piles
# left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since
# it's larger. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]

        return dp(0, 1)
        
        
# @lc code=end

