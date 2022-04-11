#
# @lc app=leetcode id=2207 lang=python3
#
# [2207] Maximize Number of Subsequences in a String
#

# @lc code=start
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        res = cnt1 = cnt2 = 0
        for c in text:
            if c == pattern[1]:
                res += cnt1
                cnt2 += 1
            
            if c == pattern[0]:
                cnt1 += 1
        return res + max(cnt1, cnt2)
        
# @lc code=end

