#
# @lc app=leetcode id=3045 lang=python3
#
# [3045] Count Prefix and Suffix Pairs II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        root = (T := lambda: defaultdict(T))()
        res = 0
        for w in words:
            x = root
            for k in zip(w, reversed(w)):
                res += (x := x[k]).get(0, 0)
            x[0] = x.get(0, 0) + 1
        return res

        
# @lc code=end

