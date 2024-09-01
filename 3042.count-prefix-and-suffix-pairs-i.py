#
# @lc app=leetcode id=3042 lang=python3
#
# [3042] Count Prefix and Suffix Pairs I
#

# @lc code=start
from itertools import combinations

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        ans = 0
        for pre_suf, word in combinations(words, 2):
            ans += word.startswith(pre_suf) and word.endswith(pre_suf)
        return ans
        
# @lc code=end

