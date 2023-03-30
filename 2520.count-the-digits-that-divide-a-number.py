#
# @lc app=leetcode id=2520 lang=python3
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        # return sum(1 if num % int(d) == 0 else 0 for d in str(num))
        return sum(num % int(d) == 0 for d in str(num))
        
# @lc code=end

