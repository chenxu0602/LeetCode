#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
#
# algorithms
# Hard (57.61%)
# Likes:    206
# Dislikes: 22
# Total Accepted:    8K
# Total Submissions: 13.9K
# Testcase Example:  '1'
#
# Given n orders, each order consist in pickup and delivery services. 
# 
# Count all valid pickup/delivery possible sequences such that delivery(i) is
# always after of pickup(i). 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 6
# Explanation: All possible orders: 
# (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and
# (P2,D2,P1,D1).
# This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery
# 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: 90
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 500
# 
# 
#

# @lc code=start
import math

class Solution:
    def countOrders(self, n: int) -> int:
        # The total number of all permutation obviously eauqls to 2n!.
        # For each pair, the order is determined, so we need to divide by 2.
        # So the final result is (2n)!/(2^n)
        return (math.factorial(n * 2) >> n) % (10**9 + 7)

        
# @lc code=end

