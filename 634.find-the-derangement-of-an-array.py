#
# @lc app=leetcode id=634 lang=python3
#
# [634] Find the Derangement of An Array
#
# https://leetcode.com/problems/find-the-derangement-of-an-array/description/
#
# algorithms
# Medium (40.05%)
# Likes:    135
# Dislikes: 120
# Total Accepted:    6.8K
# Total Submissions: 17K
# Testcase Example:  '1'
#
# 
# In combinatorial mathematics, a derangement is a permutation of the elements
# of a set, such that no element appears in its original position.
# 
# 
# 
# There's originally an array consisting of n integers from 1 to n in ascending
# order, you need to find the number of derangement it can generate.
# 
# 
# 
# Also, since the answer may be very large, you should return the output mod
# 10^9 + 7.
# 
# 
# Example 1:
# 
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1]
# and [3,1,2].
# 
# 
# 
# Note:
# n is in the range of [1, 10^6].
# 
#

# @lc code=start
class Solution:
    def findDerangement(self, n: int) -> int:
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # if n == 0: return 1
        # if n == 1: return 0
        # dp = [0] * (n + 1)
        # dp[0] = 1; dp[1] = 0

        # for i in range(2, n + 1):
        #     dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % (10**9 + 7)

        # return dp[n]



        # Time  complexity: O(n)
        # Space complexity: O(n)
        if n == 0: return 1
        if n == 1: return 0
        first, second = 1, 0
        for i in range(2, n + 1):
            first, second = second, (i - 1) * (first + second) % (10**9 + 7)

        return second


        # n! - n!/1! + n!/2! - n!/3! + ... + (-1)^n x n!/n!
        # mul, sum, M = 1, 0, 10**9 + 7
        # for i in range(n, -1, -1):
        #     if i % 2 == 0:
        #         sum = (sum + M + mul) % M
        #     else:
        #         sum = (sum + M - mul) % M
                
        #     mul = (mul * i) % M
            
        # return sum
        
# @lc code=end

