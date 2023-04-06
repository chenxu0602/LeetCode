#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:

        s = str(n)
        ans = 0

        for i in range(0, len(s), 2):
            ans += int(s[i])

        for i in range(1, len(s), 2):
            ans -= int(s[i])

        return ans
        
# @lc code=end

