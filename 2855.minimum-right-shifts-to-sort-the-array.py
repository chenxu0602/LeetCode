#
# @lc app=leetcode id=2855 lang=python3
#
# [2855] Minimum Right Shifts to Sort the Array
#

# @lc code=start
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                return n - i if nums == sorted(nums) else -1

        return 0
        
# @lc code=end

