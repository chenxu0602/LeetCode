#
# @lc app=leetcode id=2478 lang=python3
#
# [2478] Number of Beautiful Partitions
#

# @lc code=start
from functools import lru_cache

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:

        n = len(s)
        primes = set("2357")
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(i, start, k):
            if i == n: return int(k == 0)
            if i > n or k == 0 or s[i] not in primes and start: return 0
            if s[i] in primes:
                if start: 
                    return dp(i + minLength - 1, False, k)
                else:
                    return dp(i + 1, False, k)

            return (dp(i + 1, True, k - 1) + dp(i + 1, False, k)) % MOD


        return dp(0, True, k)

        
# @lc code=end

