#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (42.81%)
# Likes:    770
# Dislikes: 38
# Total Accepted:    46.9K
# Total Submissions: 108.7K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of
# coin.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# 
# Input: amount = 10, coins = [10] 
# Output: 1
# 
# 
# 
# 
# Note:
# 
# You can assume that
# 
# 
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# 
# 
#
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        """
        The reason behind that is that as you mentioned, 
        the problem is to find the total number of combinations, 
        not the permutations. 
        If the outer loop is the amount, 
        then the same combination will be counted 
        multiple times because they can come in in different 
        orders. By letting the coins to be the outer loops, 
        one assures that for any valid combination, 
        the order of each coin will always be the same as 
        their order in coins, so there can be no duplicates.
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
           for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j-i]

        return dp[amount]
        

