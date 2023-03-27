#
# @lc app=leetcode id=2506 lang=python3
#
# [2506] Count Pairs Of Similar Strings
#

# @lc code=start
from collections import Counter 
from functools import reduce

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        ans = 0
        freq = Counter()
        for word in words:
            mask = reduce(or_, (1 << ord(ch) - 97 for ch in word))
            ans += freq[mask]
            freq[mask] += 1
        return ans
        
# @lc code=end

