#
# @lc app=leetcode id=2801 lang=python3
#
# [2801] Count Stepping Numbers in Range
#

# @lc code=start
from functools import lru_cache

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:

        MOD = 10 ** 9 + 7

        def count(n: str) -> int:
            @lru_cache(None)
            def dp(i, tight, last_digit, leading_zero):
                if i == len(n): return 1
                maxDigit = int(n[i]) if tight else 9

                ans = 0
                for d in range(maxDigit + 1):
                    nxtTight = tight and d == maxDigit
                    nextLeadingZero = leading_zero and d == 0

                    if nextLeadingZero:
                        ans = (ans + dp(i + 1, nxtTight, last_digit, nextLeadingZero)) % MOD
                    elif last_digit == -1 or abs(last_digit - d) == 1:
                        ans = (ans + dp(i + 1, nxtTight, d, nextLeadingZero)) % MOD

                return ans

            return dp(0, True, -1, True)

        return (count(high) - count(str(int(low) - 1))) % MOD

        
# @lc code=end

