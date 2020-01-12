#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (29.51%)
# Likes:    215
# Dislikes: 72
# Total Accepted:    8.2K
# Total Submissions: 27.7K
# Testcase Example:  '3\n0'
#
# Given two integers n and k, find how many different arrays consist of numbers
# from 1 to n such that there are exactly k inverse pairs.
# 
# We define an inverse pair as following: For ith and jth element in the array,
# if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
# 
# Since the answer may be very large, the answer should be modulo 10^9 + 7.
# 
# Example 1:
# 
# 
# Input: n = 3, k = 0
# Output: 1
# Explanation: 
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0
# inverse pair.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 3, k = 1
# Output: 2
# Explanation: 
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# 
# 
# 
# 
# Note:
# 
# 
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
# 
# 
# 
# 
#
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k+1)
        M = 10**9 + 7
        for i in range(1, n+1):
            temp = [0] * (k+1)
            temp[0] = 1
            for j in range(1, k+1):
                val = dp[j]
                if j - i >= 0:
                    val = (dp[j] + M - dp[j-i]) % M
                temp[j] = (temp[j-1] + val) % M
            dp = temp

        if k > 0:
            return (dp[k] + M - dp[k-1]) % M
        else:
            return dp[k]
        

