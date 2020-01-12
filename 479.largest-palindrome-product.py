#
# @lc app=leetcode id=479 lang=python3
#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Hard (27.53%)
# Likes:    73
# Dislikes: 1227
# Total Accepted:    15K
# Total Submissions: 54.6K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# 
# Since the result could be very large, you should return the largest
# palindrome mod 1337.
# 
# 
# 
# Example:
# 
# Input: 2
# 
# Output: 987
# 
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# 
# 
# 
# Note:
# 
# The range of n is [1,8].
# 
#
import math

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        if n == 2: return 987

        for i in range(2, 9*10**(n-1)):
            hi = (10**n) - i
            lo = int(str(hi)[::-1])
            if i**2 - 4*lo < 0:
                continue
            if math.sqrt(i**2 - 4*lo) == int(math.sqrt(i**2 - 4*lo)):
                return (lo + 10**n*(10**n-i)) % 1337


