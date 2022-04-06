#
# @lc app=leetcode id=2160 lang=python3
#
# [2160] Minimum Sum of Four Digit Number After Splitting Digits
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:

        nums = list(map(int, sorted(str(num))))

        num1 = nums[0] * 10 + nums[2]
        num2 = nums[1] * 10 + nums[3]

        return num1 + num2
        
# @lc code=end

