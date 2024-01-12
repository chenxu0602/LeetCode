#
# @lc app=leetcode id=2949 lang=python3
#
# [2949] Count Beautiful Substrings II
#

# @lc code=start
from collections import Counter
from itertools import count

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        # Notice that if s[x+1:y] and s[x+1:z] are both beautiful (y < z), then s[y+1:z] is also beautiful. 

        n = len(s)
        l = next(i for i in count(1) if i * i % k == 0) * 2
        vowels = set(list('aeiou'))
        seen = [Counter() for i in range(l)]
        seen[-1][0] = 1
        res = v = 0

        for i, c in enumerate(s):
            v += 1 if s[i] in vowels else -1
            res += seen[i % l][v]
            seen[i % l][v] += 1

        return res
        
# @lc code=end

