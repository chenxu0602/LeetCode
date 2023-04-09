#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:

        s = "".join(sorted(str(num)))
        return int(s[::2]) + int(s[1::2])
        
# @lc code=end

