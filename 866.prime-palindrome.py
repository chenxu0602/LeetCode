#
# @lc app=leetcode id=866 lang=python3
#
# [866] Prime Palindrome
#
# https://leetcode.com/problems/prime-palindrome/description/
#
# algorithms
# Medium (20.37%)
# Likes:    97
# Dislikes: 282
# Total Accepted:    8.3K
# Total Submissions: 40.8K
# Testcase Example:  '6'
#
# Find the smallest prime palindrome greater than or equal to N.
# 
# Recall that a number is prime if it's only divisors are 1 and itself, and it
# is greater than 1. 
# 
# For example, 2,3,5,7,11 and 13 are primes.
# 
# Recall that a number is a palindrome if it reads the same from left to right
# as it does from right to left. 
# 
# For example, 12321 is a palindrome.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 6
# Output: 7
# 
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 11
# 
# 
# 
# Example 3:
# 
# 
# Input: 13
# Output: 101
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^8
# The answer is guaranteed to exist and be less than 2 * 10^8.
# 
# 
#
class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans 

        while True:
            if N == reverse(N) and is_prime(N):
                return N

            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
        

