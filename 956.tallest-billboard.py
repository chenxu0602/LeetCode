#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (39.68%)
# Likes:    356
# Dislikes: 13
# Total Accepted:    8.1K
# Total Submissions: 20.4K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height.  The
# billboard will have two steel supports, one on each side.  Each steel support
# must be an equal height.
# 
# You have a collection of rods which can be welded together.  For example, if
# you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
# 
# Return the largest possible height of your billboard installation.  If you
# cannot support the billboard, return 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# The sum of rods is at most 5000.
# 
# 
#

# @lc code=start
from functools import lru_cache
from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # Dynamic Programming
        # Let dp[i][s] be the largest score we can get using rods[j] (j >= i), 
        # after previously writing a sum of s.
        # Time  complexity: O(N x S), where N is the length of rods and S is the maximum of sum(rods).
        # Space complexity: O(N x S)
        # @lru_cache(None)
        # def dp(i, s):
        #     if i == len(rods):
        #         return 0 if s == 0 else float("-inf")
        #     return max(dp(i + 1, s),
        #                dp(i + 1, s - rods[i]),
        #                dp(i + 1, s + rods[i]) + rods[i])
        # return dp(0, 0)


        # dp[d] mean the maximum pair of sum we can get with pair difference d
        # For example, if have a pair of sum (a, b) with a > b, then dp[a - b] = b
        # If we have dp[diff] = a, it means we have a pair of sum (a, a + diff).
        # And this is the biggest pair with difference = a
        dp = defaultdict(int)
        dp[0] = 0
        for x in rods:
            for d, y in dp.copy().items():
                dp[d + x] = max(dp[d + x], y)
                dp[abs(d - x)] = max(dp[abs(d - x)], y + min(d, x))
        return dp[0]
        
# @lc code=end

