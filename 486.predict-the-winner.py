#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (46.85%)
# Likes:    1015
# Dislikes: 67
# Total Accepted:    51.5K
# Total Submissions: 109.9K
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
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2
# (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 +
# 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you
# need to return False.
# 
# 
# 
# Example 2:
# 
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose
# 233.Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
# 
# 
# 
# Note:
# 
# 1 
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
# 
# 
#
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
#        return self.winner(nums, 0, len(nums) - 1, 1) >= 0

        n = len(nums)
        dp = [[0] * n for _ in range(n+1)]
        for s in range(n, -1, -1):
            for e in range(s+1, n):
                a = nums[s] - dp[s+1][e]
                b = nums[e] - dp[s][e-1]
                dp[s][e] = max(a, b)

        return dp[0][n-1] >= 0

         

    def winner(self, nums, s, e, turn):
        if s == e:
            return turn * nums[s]

        a = turn * nums[s] + self.winner(nums, s + 1, e, -turn)
        b = turn * nums[e] + self.winner(nums, s, e - 1, -turn)

        return turn * max(turn * a, turn * b)
        

