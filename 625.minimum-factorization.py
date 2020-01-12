#
# @lc app=leetcode id=625 lang=python3
#
# [625] Minimum Factorization
#
# https://leetcode.com/problems/minimum-factorization/description/
#
# algorithms
# Medium (32.18%)
# Likes:    70
# Dislikes: 56
# Total Accepted:    6.7K
# Total Submissions: 20.8K
# Testcase Example:  '48'
#
# Given a positive integer a, find the smallest positive integer b whose
# multiplication of each digit equals to a. 
# 
# 
# If there is no answer or the answer is not fit in 32-bit signed integer, then
# return 0.
# 
# 
# Example 1
# Input:
# 48 
# Output:
# 68
# 
# 
# 
# Example 2
# Input: 
# 15
# 
# Output:
# 35
# 
#
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 2:
            return a

        res, mul = 0, 1
        for i in range(9, 1, -1):
            while a % i == 0:
                a /= i
                res = mul * i + res
                mul *= 10

        return int(res) if a < 2 and res < (1 << 31) else 0
        

