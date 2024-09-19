#
# @lc app=leetcode id=3258 lang=python3
#
# [3258] Count Substrings That Satisfy K-Constraint I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        res, l, ones = 0, 0, 0
        for r, c in enumerate(s):
            ones += 1 if c == '1' else 0
            while ones > k and r - l + 1 - ones > k:
                ones -= 1 if s[l] == '1' else 0
                l += 1

            res += r - l + 1

        return res
        
# @lc code=end

