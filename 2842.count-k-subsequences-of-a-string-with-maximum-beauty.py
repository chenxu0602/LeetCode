#
# @lc app=leetcode id=2842 lang=python3
#
# [2842] Count K-Subsequences of a String With Maximum Beauty
#

# @lc code=start
from collections import Counter
from math import comb

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:

        count = Counter(s)
        if len(count) < k: return 0

        bar = sorted(count.values())[-k]
        res = 1
        MOD = 10**9 + 7
        m = 0

        for v in count.values():
            if v > bar:
                k -= 1
                res = res * v % MOD

            if v == bar:
                m += 1

        return res * comb(m, k) * pow(bar, k, MOD) % MOD
        
# @lc code=end

