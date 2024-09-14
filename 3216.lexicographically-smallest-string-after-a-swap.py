#
# @lc app=leetcode id=3216 lang=python3
#
# [3216] Lexicographically Smallest String After a Swap
#

# @lc code=start
from itertools import pairwise

class Solution:
    def getSmallestString(self, s: str) -> str:

        n, s = len(s), list(s)
        for i, j in pairwise(range(n)):
            if s[i] > s[j] and (ord(s[i]) - ord(s[j])) % 2 == 0:
                s[i], s[j] = s[j], s[i]
                break

        return ''.join(s)
        
# @lc code=end

