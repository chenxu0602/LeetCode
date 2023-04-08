#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#

# @lc code=start
from itertools import accumulate

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = lambda w: w[0] in "aeiou" and w[-1] in "aeiou"
        words = map(vowels, words)
        prefix = list(accumulate(words, initial=0)) # add 0 at the front

        return [prefix[r + 1] - prefix[l] for l, r in queries]
        
# @lc code=end

