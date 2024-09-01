#
# @lc app=leetcode id=3035 lang=python3
#
# [3035] Maximum Palindromes After Operations
#

# @lc code=start
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:

        count = Counter([c for w in words for c in w])
        res = 0
        pairs = sum(char_cnt // 2 for char_cnt in count.values())
        for sz in sorted([len(w) for w in words]):
            pairs -= sz // 2
            res += pairs >= 0
        return res
        
# @lc code=end

