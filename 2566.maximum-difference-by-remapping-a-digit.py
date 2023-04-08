#
# @lc app=leetcode id=2566 lang=python3
#
# [2566] Maximum Difference by Remapping a Digit
#

# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:

        num = str(num)
        i = 0
        while num[i] == '9' and i < len(num) - 1:
            i += 1

        return int(num.replace(num[i], '9')) - int(num.replace(num[0], '0'))
        
# @lc code=end

