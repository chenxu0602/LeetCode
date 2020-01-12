#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (44.08%)
# Likes:    1347
# Dislikes: 48
# Total Accepted:    92.5K
# Total Submissions: 209.7K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        free, have, cool = 0, float("-inf"), float("-inf")
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p

        return max(free, cool)
        """

        p1, p2 = 0, 0
        for i in range(1, len(prices)):
            temp = p1
            p1 = max(p1 + prices[i] - prices[i-1], p2)
            p2 = max(temp, p2)

        return max(p1, p2)


        

