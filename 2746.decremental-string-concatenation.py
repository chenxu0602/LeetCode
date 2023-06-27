#
# @lc app=leetcode id=2746 lang=python3
#
# [2746] Decremental String Concatenation
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        @lru_cache(None)
        def dp(l, r, i): 
            if i == len(words): return 0

            L, R = words[i][0], words[i][-1]

            return max((R == l) + dp(L, r, i + 1),
                       (r == L) + dp(l, R, i + 1))

        return sum(map(len, words)) - dp(words[0][0], words[0][-1], 1)
        
# @lc code=end

