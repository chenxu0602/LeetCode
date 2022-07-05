#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#

# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        i = 0
        while int(s[-i - 1:], 2) <= k and i < 32 and i < len(s):
            i += 1
        return s[:-i].count('0') + i
# @lc code=end

