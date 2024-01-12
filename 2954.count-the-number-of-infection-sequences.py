#
# @lc app=leetcode id=2954 lang=python3
#
# [2954] Count the Number of Infection Sequences
#

# @lc code=start
from functools import cache
from itertools import pairwise

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        MOD = 10**9 + 7

        @cache
        def fact(i): return 1 if i < 2 else i * fact(i - 1) % MOD

        @cache
        def ifact(i): return pow(fact(i), -1, MOD)

        res = fact(n - len(sick)) * ifact(sick[0]) * ifact(n - sick[-1] - 1) % MOD
        for group in [b - a - 1 for a, b in pairwise(sick) if b - a > 1] :
            res = res * ifact(group) % MOD
            res = res * pow(2, group - 1, MOD) % MOD

        return res
        
# @lc code=end

