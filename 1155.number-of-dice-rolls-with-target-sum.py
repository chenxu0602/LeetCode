#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (49.16%)
# Likes:    907
# Dislikes: 45
# Total Accepted:    52K
# Total Submissions: 108.1K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# 
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
# 
# 
# Example 1:
# 
# 
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
# 
# 
# Example 4:
# 
# 
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# 
# 
# Example 5:
# 
# 
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= d, f <= 30
# 1 <= target <= 1000
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # @lru_cache(None)
        # def dp(d, target):
        #     if d == 0:
        #         return 0 if target > 0 else 1

        #     if target > d * (1 + f) // 2:
        #         return dp(d, d * (1 + f) - target)

        #     res = 0
        #     for k in range(max(0, target - f), target):
        #         res += dp(d - 1, k)

        #     return res

        # return dp(d, target) % (10**9 + 7)


        # Similar to #518 coins
        dp = [1] + [0] * target 
        for i in range(d):
            for j in range(target, -1, -1):
                dp[j] = sum(dp[max(0, j - f):j])
        return dp[target] % (10**9 + 7)

# @lc code=end

