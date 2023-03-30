#
# @lc app=leetcode id=2513 lang=python3
#
# [2513] Minimize the Maximum of Two Arrays
#

# @lc code=start
import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:

        """
        # Let's f(u,d)f(u, d)f(u,d) is the minimum possible maximum integer in an array of size u that are not divisible by divisor d. 
        def f(u, d): return u + (u - 1) // (d - 1)
        return max(f(uniqueCnt1, divisor1), f(uniqueCnt2, divisor2), f(uniqueCnt1 + uniqueCnt2, math.lcm(divisor1, divisor2)))
        """

        lo, hi = 0, 1 << 32 - 1
        mult = math.lcm(divisor1, divisor2)

        while lo < hi:
            mi = lo + hi >> 1
            if uniqueCnt1 <= mi - mi // divisor1 and uniqueCnt2 <= mi - mi // divisor2 and uniqueCnt1 + uniqueCnt2 <= mi - mi // mult:
                hi = mi
            else:
                lo = mi + 1
        return lo
        
# @lc code=end

