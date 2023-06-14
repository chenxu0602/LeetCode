#
# @lc app=leetcode id=2730 lang=python3
#
# [2730] Find the Longest Semi-Repetitive Substring
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        res, tab = 0, [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tab += 1,
            else:
                tab[-1] += 1

        for j in range(1, len(tab)):
            res = max(res, tab[j] + tab[j - 1])

        return max(res, tab[0])

        
# @lc code=end

