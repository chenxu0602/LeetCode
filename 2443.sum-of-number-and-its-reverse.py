#
# @lc app=leetcode id=2443 lang=python3
#
# [2443] Sum of Number and Its Reverse
#

# @lc code=start
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num // 2, num + 1):
            strN = str(n)
            strR = strN[::-1]
            if int(strN) + int(strR) == num:
                return True

        return False

        
# @lc code=end

