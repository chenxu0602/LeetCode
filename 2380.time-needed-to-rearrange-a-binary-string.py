#
# @lc app=leetcode id=2380 lang=python3
#
# [2380] Time Needed to Rearrange a Binary String
#

# @lc code=start
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        """
        ans = prefix = prev = 0
        for i, c in enumerate(s):
            if c == '1':
                ans = max(prev, i - prefix)
                prefix += 1
                if ans:
                    prev = ans + 1
        return ans
        """

        zeros = seconds = 0
        for i in range(len(s)):
            zeros += s[i] == '0'
            if s[i] == '1' and zeros:
                seconds = max(seconds + 1, zeros)

        return seconds
        
# @lc code=end

