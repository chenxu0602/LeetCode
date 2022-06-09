#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for test in [str(i) * 3 for i in range(9, -1, -1)]:
            if test in num:
                return test
        return ""
        
# @lc code=end

