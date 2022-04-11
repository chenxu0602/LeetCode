#
# @lc app=leetcode id=2186 lang=python3
#
# [2186] Minimum Number of Steps to Make Two Strings Anagram II
#

# @lc code=start
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        return sum(abs(s[ch] - t[ch]) for ch in "abcdefghijklmnopqrstuvwxyz")

        
# @lc code=end

