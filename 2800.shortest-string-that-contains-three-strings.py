#
# @lc app=leetcode id=2800 lang=python3
#
# [2800] Shortest String That Contains Three Strings
#

# @lc code=start
from itertools import permutations

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:

        def merge(s1, s2):
            if s1 == s2 or s2 in s1:
                return s1
            elif s1 in s2:
                return s2 
            else:
                for i in range(len(s1)):
                    if s2.startswith(s1[i:]):
                        return s1[:i] + s2

            return s1 + s2

        
        strings = [a, b, c]
        results = []
        for p in permutations(strings):
            merged = merge(merge(p[0], p[1]), p[2])
            results += merged,

        return min(results, key=lambda x: (len(x), x))
        
# @lc code=end

