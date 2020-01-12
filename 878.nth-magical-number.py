#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#
# https://leetcode.com/problems/nth-magical-number/description/
#
# algorithms
# Hard (25.75%)
# Likes:    126
# Dislikes: 43
# Total Accepted:    6.2K
# Total Submissions: 23.8K
# Testcase Example:  '1\n2\n3'
#
# A positive integer is magical if it is divisible by either A or B.
# 
# Return the N-th magical number.  Since the answer may be very large, return
# it modulo 10^9 + 7.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 1, A = 2, B = 3
# Output: 2
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 4, A = 2, B = 3
# Output: 6
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 5, A = 2, B = 4
# Output: 10
# 
# 
# 
# Example 4:
# 
# 
# Input: N = 3, A = 6, B = 4
# Output: 8
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 2 <= A <= 40000
# 2 <= B <= 40000
# 
# 
# 
# 
# 
# 
#
from fractions import gcd

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:

        """
        MAX_NUM = pow(10, 9) + 7

        def gcd(A, B):
            if A < B:
                A, B = B, A
            while B:
                A, B = B, A % B
            return A

        def lcm(A, B):
            return (A * B) // gcd(A, B)

        lcm_val = lcm(A, B)
        unit_list = []
        M = (lcm_val // A) + (lcm_val // B) - 1

        i, j = 1, 1
        while i <= lcm_val // A and j <= lcm_val // B:
            if i * A < j * B:
                unit_list.append(i * A)
                i += 1
            else:
                unit_list.append(j * B)
                j += 1

        while i < lcm_val // A:
            unit_list.append(i*A)
            i += 1

        while j < lcm_val // B:
            unit_list.append(j*B)
            j += 1

        ret = (N // M)*lcm_val + unit_list[(N % M)-1] if N % M > 0 else (N // M)*lcm_val
        return ret if ret < MAX_NUM else ret % MAX_NUM
        """

        MOD = 10**9 + 7
        L = A / gcd(A, B) * B

        def magic_below_x(x):
            return x // A + x // B - x // L

        lo, hi = 0, 10**15
        while lo < hi:
            mi = (lo + hi) // 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi

        return lo % MOD
        
        

