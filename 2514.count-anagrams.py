#
# @lc app=leetcode id=2514 lang=python3
#
# [2514] Count Anagrams
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        res, MOD = 1, 10**9 + 7
        for w in s.split(' '):
            cnt, prem = Counter(w), math.factorial(len(w))
            for rep in cnt.values():
                prem //= math.factorial(rep)
            res = res * prem % MOD
        return res
        
# @lc code=end

