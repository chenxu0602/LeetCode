#
# @lc app=leetcode id=2060 lang=python3
#
# [2060] Check if an Original String Exists Given Two Encoded Strings
#

# @lc code=start
from functools import lru_cache

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        def getValidPrefixLength(s, start):
            end = start
            while end < len(s) and s[end].isdigit():
                end += 1
            return end

        @lru_cache(None)
        def possiblenLengths(s):
            ans = {int(s)}
            for i in range(1, len(s)):
                ans |= {x + y for x in possiblenLengths(s[:i]) for y in possiblenLengths(s[i:])}
            return ans

        @lru_cache(None)
        def dp(i, j, diff):
            if i == len(s1) and j == len(s2): return diff == 0

            # s1 has not reached end and s1 starts with a digit
            if i < len(s1) and s1[i].isdigit():
                i2 = getValidPrefixLength(s1, i)
                for L in possiblenLengths(s1[i:i2]):
                    if dp(i2, j, diff - L): 
                        return True
            # s2 has not reached end and s2 starts with a digit
            elif j < len(s2) and s2[j].isdigit():
                j2 = getValidPrefixLength(s2, j)
                for L in possiblenLengths(s2[j:j2]):
                    if dp(i, j2, diff + L): 
                        return True
            elif diff == 0:
                if i == len(s1) or j == len(s2) or s1[i] != s2[j]:
                    return False
                return dp(i + 1, j + 1, 0)
            elif diff > 0:
                # no s1 to balance s2's lead
                if i == len(s1): return False
                return dp(i + 1, j, diff - 1)
            else:
                # no s2 to balance s1's lead
                if j == len(s2): return False
                return dp(i, j + 1, diff + 1)

        return dp(0, 0, 0)
        
# @lc code=end

