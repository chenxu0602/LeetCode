#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#
# https://leetcode.com/problems/nth-magical-number/description/
#
# algorithms
# Hard (28.38%)
# Likes:    220
# Dislikes: 63
# Total Accepted:    9.9K
# Total Submissions: 34.6K
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

# @lc code=start
from fractions import gcd

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        # Mathematical
        # Let L be the least common multiple of A and B. 
        # There are M = L/A + L/B - 1 magical numbers less than or equal to L.
        # L/A of them are divisible by A, L/B of the m are divisible by B, and 1 of them is divisible by both.
        # Time  complexity: O(A + B)
        # Space complexity: O(1)
        # MOD = 10**9 + 7

        # L = A * B // gcd(A, B)
        # M = L // A + L // B - 1
        # q, r = divmod(N, M)

        # if r == 0: return q * L % MOD

        # heads = [A, B]
        # for _ in range(r - 1):
        #     if heads[0] <= heads[1]:
        #         heads[0] += A
        #     else:
        #         heads[1] += B

        # return (q * L + min(heads)) % MOD


        # Binary Search
        # Time  complexity: O(log(N x min(A, B)))
        # Space complexity: O(1)
        MOD = 10**9 + 7
        L = A * B // gcd(A, B)

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

        
# @lc code=end

