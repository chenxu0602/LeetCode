#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        digitSum = sum(map(int, list(''.join(map(str, nums)))))
        return sum(nums) - digitSum
        
# @lc code=end

