#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (45.52%)
# Likes:    1885
# Dislikes: 73
# Total Accepted:    119.3K
# Total Submissions: 262K
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

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Time  complexity: O(N)
        # Space complexity: O(1)
        sold, held, reset = float("-inf"), float("-inf"), 0

        for price in prices:
            sold, held, reset = held + price, max(held, reset - price), max(reset, sold)

        return max(sold, reset)


        # p1, p2 = 0, 0
        # for i in range(1, len(prices)):
        #     temp = p1
        #     p1 = max(p1 + prices[i] - prices[i-1], p2)
        #     p2 = max(temp, p2)

        # return max(p1, p2)
        
# @lc code=end

