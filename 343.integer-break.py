#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (47.83%)
# Likes:    585
# Dislikes: 169
# Total Accepted:    80.7K
# Total Submissions: 168.4K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
# 
# Example 1:
# 
# 
# 
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# Note: You may assume that n is not less than 2 and not larger than 58.
# 
# 
#
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        if n == 2: 
            return 1

        if n == 3:
            return 2

        dp = [0] * (n + 1)

        dp[2] = 2;
        dp[3] = 3;

        for i in range(4, n+1):
            dp[i] = max(dp[i-2] * 2, dp[i-3] * 3)

        return dp[n]
        """

        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 3**(n//3 - 1) * 4
        if n % 3 == 2:
            return 3**(n//3) * 2



        """

        if n == 2:
            return 1

        if n == 3:
            return 2

        res = 1

        while n > 2:
            res *= 3
            n -= 3

        if n == 0:
            return res

        if n == 1:
            return (res // 3) * 4

        if n == 2:
            return res * 2

        """
        

        

