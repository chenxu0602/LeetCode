#
# @lc app=leetcode id=2235 lang=python3
#
# [2235] Add Two Integers
#

# @lc code=start
import operator

class Solution:
    def sum(self, num1: int, num2: int) -> int:

        # mask = 0xFFFFFFFF

        # while num2 != 0:
        #     num1, num2 = (num1 ^ num2) & mask, ((num1 & num2) << 1) ^ mask

        # max_int = 0x7FFFFFFF
        # return num1 if num1 < max_int else ~(num1 ^ mask)

        return operator.add(num1, num2)

        
# @lc code=end

