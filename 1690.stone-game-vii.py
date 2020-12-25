#
# @lc app=leetcode id=1690 lang=python3
#
# [1690] Stone Game VII
#
# https://leetcode.com/problems/stone-game-vii/description/
#
# algorithms
# Medium (40.34%)
# Likes:    79
# Dislikes: 51
# Total Accepted:    3.1K
# Total Submissions: 7.6K
# Testcase Example:  '[5,3,1,4,2]'
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# There are n stones arranged in a row. On each player's turn, they can remove
# either the leftmost stone or the rightmost stone from the row and receive
# points equal to the sum of the remaining stones' values in the row. The
# winner is the one with the higher score when there are no stones left to
# remove.
# 
# Bob found that he will always lose this game (poor Bob, he always loses), so
# he decided to minimize the score's difference. Alice's goal is to maximize
# the difference in the score.
# 
# Given an array of integers stones where stones[i] represents the value of the
# i^th stone from the left, return the difference in Alice and Bob's score if
# they both play optimally.
# 
# 
# Example 1:
# 
# 
# Input: stones = [5,3,1,4,2]
# Output: 6
# Explanation: 
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0,
# stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones =
# [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones =
# [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.
# 
# 
# Example 2:
# 
# 
# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122
# 
# 
# Constraints:
# 
# 
# n == stones.length
# 2 <= n <= 1000
# 1 <= stones[i] <= 1000
# 
# 
#

# @lc code=start
from functools import lru_cache
import itertools

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # O(n^2)

        # @lru_cache(None)
        # def dp(i, j):
        #     # if (j-i+1) %2 == n%2, Alice choose first; otherwise Bob choose first.
		# 	# return the minimum of the sum of elements that Bob can choose from A[i:j+1] by playing stoneGameVII
        #     if j - i + 1 <= 0:
        #         return 0

        #     if (j - i + 1) % 2 == len(stones) % 2:
        #         # Alice choose, but what she choose don't credit to return value
        #         r = max(dp(i + 1, j), dp(i, j - 1))
        #     else:
        #         # Bob choose
        #         r = min(stones[i] + dp(i + 1, j), stones[j] + dp(i, j - 1))

        #     return r


        # res = dp(0, len(stones) - 1)
        # dp.cache_clear()
        # return res



        # pre_sum = list(itertools.accumulate([0] + stones))

        # def score(i, j):
        #     return pre_sum[j + 1] - pre_sum[i]

        # @lru_cache(None)
        # def helper(i, j):
        #     if i >= j:
        #         return 0
        #     return max(score(i + 1, j) - helper(i + 1, j), score(i, j - 1) - helper(i, j - 1))

        # res = helper(0, len(stones) - 1)
        # helper.cache_clear()
        # return res


        pre_sum = list(itertools.accumulate([0] + stones))

        def score(i, j):
            return pre_sum[j + 1] - pre_sum[i]

        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(score(i + 1, j) - dp[i + 1][j], score(i, j - 1) - dp[i][j - 1])

        return dp[0][n - 1]
        
# @lc code=end

