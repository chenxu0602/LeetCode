#
# @lc app=leetcode id=2827 lang=python3
#
# [2827] Number of Beautiful Integers in the Range
#

# @lc code=start
from functools import lru_cache

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        def helper(num, k):
            num = str(num)
            n = len(num)

            @lru_cache(None)
            def dfs(i, delta, m, tight, headzero):
                if i == n: return not headzero and (delta == 0 and m == 0)
                upper = ord(num[i]) - ord('0') if tight else 9

                res = 0
                for curdigit in range(upper + 1):
                    zerocheck = headzero and curdigit == 0
                    res += dfs(i + 1, 
                               delta + (1 if curdigit % 2 else (0 if zerocheck else -1)), 
                               (m * 10 + curdigit) % k, 
                               tight and (curdigit == upper), 
                               zerocheck)

                return res

            return dfs(0, 0, 0, 1, 1)


        return helper(high, k) - helper(low - 1, k)
        
# @lc code=end

