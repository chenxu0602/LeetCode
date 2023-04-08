#
# @lc app=leetcode id=2565 lang=python3
#
# [2565] Subsequence With the Minimum Score
#

# @lc code=start
class Solution:
    def minimumScore(self, s: str, t: str) -> int:

        n = len(s)
        suffix = [-1] * n
        j = len(t) - 1

        for i in reversed(range(n)):
            if 0 <= j and s[i] == t[j]:
                j -= 1
            suffix[i] = j

        ans = j + 1
        j = 0
        for i, c in enumerate(s):
            ans = min(ans, max(0, suffix[i] - j + 1))
            if j < len(t) and s[i] == t[j]:
                j += 1

        return min(ans, len(t) - j)
        
# @lc code=end

