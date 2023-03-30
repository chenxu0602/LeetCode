#
# @lc app=leetcode id=2516 lang=python3
#
# [2516] Take K of Each Character From Left and Right
#

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        # Counting the opposite in the middle

        limits = {c: s.count(c) - k for c in "abc"}
        if any(x < 0 for x in limits.values()): return -1

        cnts = {c: 0 for c in "abc"}
        ans = l = 0
        for i, c in enumerate(s):
            cnts[c] += 1
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)

        return len(s) - ans
        
# @lc code=end

