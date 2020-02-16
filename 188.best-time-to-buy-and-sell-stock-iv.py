#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (27.37%)
# Likes:    1119
# Dislikes: 67
# Total Accepted:    111.3K
# Total Submissions: 406.5K
# Testcase Example:  '2\n[2,4,1]'
#
# Say you have an array for which the i-th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
# 3.
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n >> 1:
            return sum([max(prices[i] - prices[i-1], 0) for i in range(1, n)])

        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            transaction = 0
            for j in range(1, n):
                profit = prices[j] - prices[j-1]
                transaction = max(dp[i-1][j-1] + max(profit, 0), transaction + profit)
                dp[i][j] = max(dp[i][j-1], transaction)

        return dp[k][-1]
        
# @lc code=end

