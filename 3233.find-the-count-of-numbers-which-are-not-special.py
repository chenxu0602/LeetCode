#
# @lc app=leetcode id=3233 lang=python3
#
# [3233] Find the Count of Numbers Which Are Not Special
#

# @lc code=start
from math import ceil, sqrt, isqrt

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        min_, max_ = ceil(sqrt(l)), isqrt(r)
        sieve = [False, False, True]
        sieve.extend([True, False] * (max_ // 2))

        for p in range(3, max_ + 1, 2):
            if not sieve[p]: continue
            for i in range(p * p, max_ + 1, p + p):
                sieve[i] = False

        return r - l + 1 - sum(sieve[min_:max_ + 1])
        
# @lc code=end

