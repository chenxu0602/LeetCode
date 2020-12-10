#
# @lc app=leetcode id=1648 lang=python3
#
# [1648] Sell Diminishing-Valued Colored Balls
#
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/description/
#
# algorithms
# Medium (30.30%)
# Likes:    152
# Dislikes: 38
# Total Accepted:    4.6K
# Total Submissions: 15.2K
# Testcase Example:  '[2,5]\n4'
#
# You have an inventory of different colored balls, and there is a customer
# that wants orders balls of any color.
# 
# The customer weirdly values the colored balls. Each colored ball's value is
# the number of balls of that color you currently have in your inventory. For
# example, if you own 6 yellow balls, the customer would pay 6 for the first
# yellow ball. After the transaction, there are only 5 yellow balls left, so
# the next yellow ball is then valued at 5 (i.e., the value of the balls
# decreases as you sell more to the customer).
# 
# You are given an integer array, inventory, where inventory[i] represents the
# number of balls of the i^th color that you initially own. You are also given
# an integer orders, which represents the total number of balls that the
# customer wants. You can sell the balls in any order.
# 
# Return the maximum total value that you can attain after selling orders
# colored balls. As the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: inventory = [2,5], orders = 4
# Output: 14
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 +
# 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
# 
# 
# Example 2:
# 
# 
# Input: inventory = [3,5], orders = 6
# Output: 19
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5
# + 4 + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
# 
# 
# Example 3:
# 
# 
# Input: inventory = [2,8,4,10,6], orders = 20
# Output: 110
# 
# 
# Example 4:
# 
# 
# Input: inventory = [1000000000], orders = 1000000000
# Output: 21
# Explanation: Sell the 1st color 1000000000 times for a total value of
# 500000000500000000. 500000000500000000 modulo 10^9 + 7 = 21.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= inventory.length <= 10^5
# 1 <= inventory[i] <= 10^9
# 1 <= orders <= min(sum(inventory[i]), 10^9)
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # O(nlogn)
        arr = sorted(Counter(inventory).items(), reverse=True) + [(0, 0)]
        ans, ind, width = 0, 0, 0

        while orders > 0:
            width += arr[ind][1]
            sell = min(orders, width * (arr[ind][0] - arr[ind + 1][0]))
            whole, remainder = divmod(sell, width)
            ans += width * (whole * (arr[ind][0] + arr[ind][0] - (whole - 1))) // 2 + remainder * (arr[ind][0] - whole)
            orders -= sell
            ind += 1
        
        return ans % (10**9 + 7)


        # fn = lambda x: sum(max(0, xx - x) for xx in inventory)

        # lo, hi = 0, 10**9
        # while lo < hi:
        #     mid = lo + hi + 1 >> 1
        #     if fn(mid) >= orders:
        #         lo = mid
        #     else:
        #         hi = mid - 1

        # ans = sum((x + lo + 1) * (x - lo) // 2 for x in inventory if x > lo)
        # return (ans - (fn(lo) - orders) * (lo + 1)) % (10**9 + 7)
        
# @lc code=end

