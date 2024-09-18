#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        one_digit = sum(filter(lambda x: x < 10, nums))
        sum_ = sum(nums)
        return sum_ % 2 != 0 or one_digit != sum_ // 2
        
# @lc code=end

