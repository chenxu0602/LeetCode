#
# @lc app=leetcode id=2318 lang=python3
#
# [2318] Number of Distinct Roll Sequences
#

# @lc code=start
from functools import lru_cache

class Solution:
    def distinctSequences(self, n: int) -> int:
        m = [[1,2,3,4,5,6], 
            [2,3,4,5,6],
            [1,3,5],
            [1,2,4,5],
            [1,3,5],
            [1,2,3,4,6],
            [1,5]]
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(prev, pprev, n):
            if n == 0: return 1
            return sum(dp(x, prev, n - 1) for x in m[prev] if pprev != x) % MOD
        return dp(0, 0, n)
        
        
# @lc code=end

