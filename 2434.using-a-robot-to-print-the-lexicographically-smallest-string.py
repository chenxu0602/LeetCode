#
# @lc app=leetcode id=2434 lang=python3
#
# [2434] Using a Robot to Print the Lexicographically Smallest String
#

# @lc code=start
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        cnt, lo, p, t = Counter(s), 'a', [], []
        for c in s:
            t += c
            cnt[c] -= 1

            while lo < 'z' and cnt[lo] == 0:
                lo = chr(ord(lo) + 1)
            
            while t and t[-1] <= lo:
                p += t.pop()

        return "".join(p)
        
# @lc code=end

