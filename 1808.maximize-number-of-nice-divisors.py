#
# @lc app=leetcode id=1808 lang=python3
#
# [1808] Maximize Number of Nice Divisors
#
# https://leetcode.com/problems/maximize-number-of-nice-divisors/description/
#
# algorithms
# Hard (25.82%)
# Likes:    78
# Dislikes: 93
# Total Accepted:    2.7K
# Total Submissions: 10.2K
# Testcase Example:  '5'
#
# You are given a positive integer primeFactors. You are asked to construct a
# positive integer n that satisfies the following conditions:
# 
# 
# ⁠ The number of prime factors of n (not necessarily distinct) is at most
# primeFactors.
# ⁠ The number of nice divisors of n is maximized. Note that a divisor of n is
# nice if it is divisible by every prime factor of n. For example, if n = 12,
# then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3
# and 4 are not.
# 
# 
# Return the number of nice divisors of n. Since that number can be too large,
# return it modulo 10^9 + 7.
# 
# Note that a prime number is a natural number greater than 1 that is not a
# product of two smaller natural numbers. The prime factors of a number n is a
# list of prime numbers such that their product equals n.
# 
# 
# Example 1:
# 
# 
# Input: primeFactors = 5
# Output: 6
# Explanation: 200 is a valid value of n.
# It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors:
# [10,20,40,50,100,200].
# There is not other value of n that has at most 5 prime factors and more nice
# divisors.
# 
# 
# Example 2:
# 
# 
# Input: primeFactors = 8
# Output: 18
# 
# 
# 
# Constraints:
# 
# 
# 1 <= primeFactors <= 10^9
# 
#

# @lc code=start
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # m = p1^a1 x p2^a2 ... x pk^ak
        # a1 + a2 + ... + ak <= n
        # result = a1 x a2 x ... x ak
        MOD = 10**9 + 7
        if primeFactors <= 3: return primeFactors 
        if primeFactors % 3 == 0: return pow(3, primeFactors // 3, MOD)
        if primeFactors % 3 == 1: return (pow(3, (primeFactors - 4) // 3, MOD) * 4) % MOD
        return (2 * pow(3, primeFactors // 3, MOD)) % MOD
        
# @lc code=end

