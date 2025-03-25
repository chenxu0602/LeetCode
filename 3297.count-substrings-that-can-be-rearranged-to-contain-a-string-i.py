#
# @lc app=leetcode id=3297 lang=python3
#
# [3297] Count Substrings That Can Be Rearranged to Contain a String I
#

# @lc code=start
from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:

        counts = Counter(word2)
        matches, res, j = len(counts), 0, 0
        for i, c in enumerate(word1):
            counts[c] -= 1
            matches -= counts[c] == 0
            while matches == 0:
                matches += counts[word1[j]] == 0
                counts[word1[j]] += 1
                j += 1
            res += j

        return res
        
# @lc code=end

