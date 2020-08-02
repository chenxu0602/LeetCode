#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (35.96%)
# Likes:    1645
# Dislikes: 64
# Total Accepted:    187.2K
# Total Submissions: 520.3K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Time/Space complexity: O(N)
        # if len(prices) < 2: return 0

        # profits, max_profit, current_min = [], float("-inf"), float("inf")
        # for p in prices:
        #     current_min = min(current_min, p)
        #     max_profit = max(max_profit, p - current_min)
        #     profits.append(max_profit)

        # total_max, max_profit, current_max = float("-inf"), float("-inf"), float("-inf")
        # for i in range(len(prices)-1, -1, -1):
        #     current_max = max(current_max, prices[i])
        #     max_profit = max(max_profit, current_max - prices[i])
        #     total_max = max(total_max, profits[i] + max_profit)

        # return total_max

        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

        
# @lc code=end

