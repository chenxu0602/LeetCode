#
# @lc app=leetcode id=2791 lang=python3
#
# [2791] Count Paths That Can Form a Palindrome in a Tree
#

# @lc code=start
from collections import Counter
from functools import lru_cache

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:

        @lru_cache(None)
        def f(i):
            return f(parent[i]) ^ (1 << (ord(s[i]) - ord('a'))) if i else 0

        count = Counter()
        res = 0
        for i in range(len(parent)):
            v = f(i)
            res += count[v] + sum(count[v ^ (1 << j)] for j in range(26))
            count[v] += 1
        return res

        
# @lc code=end

