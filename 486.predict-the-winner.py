#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (47.88%)
# Likes:    1539
# Dislikes: 89
# Total Accepted:    71.2K
# Total Submissions: 148.7K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins.
# 
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score.
# 
# Example 1:
# 
# 
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
# player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return False.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Recursion
        # Time  complexity: O(2^n) if no cache. O(n^2) with cache. Size of recursion tree will be 2^n. Here, n refers to the length of nums array.
        # Space complexity: O(n) if no cache. The depth of recursion tree can go upto n. O(n^2) with cache.
        # @lru_cache(None)
        # def winner(s, e, turn):
        #     if s == e:
        #         return turn * nums[s]

        #     a = turn * nums[s] + winner(s + 1, e, -turn)
        #     b = turn * nums[e] + winner(s, e - 1, -turn)

        #     return turn * max(turn * a, turn * b)
        #     # return max(a, b) if turn == 1 else min(a, b)

        # return winner(0, len(nums) - 1, 1) >= 0



        # Dynamic Programming 
        # Time  complexity: O(n^2)
        # Space complexity: O(n^2)
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        # for s in range(n - 1, -1, -1):
        #     dp[s][s] = nums[s]
        #     for e in range(s + 1, n):
        #         a = nums[s] - dp[s + 1][e]
        #         b = nums[e] - dp[s][e - 1]
        #         dp[s][e] = max(a, b)
        # return dp[0][n - 1] >= 0


        # 1-D Dynamic Programming 
        # Time  complexity: O(n^2)
        # Space complexity: O(n)
        dp = [0] * len(nums)
        for s in range(len(nums) - 1, -1, -1):
            dp[s] = nums[s]
            for e in range(s + 1, len(nums)):
                a = nums[s] - dp[e]
                b = nums[e] - dp[e - 1]
                dp[e] = max(a, b)
        return dp[-1] >= 0
        

# @lc code=end

