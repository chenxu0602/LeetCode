#
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number
#

# @lc code=start
class Solution:
    def smallestNumber(self, num: int) -> int:

        s = sorted(str(abs(num)), reverse=num < 0)
        non_zero = next((i for i, n in enumerate(s) if n != '0'), 0)
        s[0], s[non_zero] = s[non_zero], s[0]
        return int(''.join(s)) * (1 if num >= 0 else -1)
        
# @lc code=end

