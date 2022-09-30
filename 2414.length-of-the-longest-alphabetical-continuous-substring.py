#
# @lc app=leetcode id=2414 lang=python3
#
# [2414] Length of the Longest Alphabetical Continuous Substring
#

# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        cur = res = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                cur = cur + 1
                res = max(cur, res)
            else:
                cur = 1

        return res
        
# @lc code=end

