#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#

# @lc code=start
from functools import reduce
from operator import mul

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for i in range(n, n + 10):
            if reduce(mul, map(int, str(i))) % t == 0:
                return i
        
# @lc code=end

