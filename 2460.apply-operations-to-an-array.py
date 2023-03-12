#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1], nums[i] = nums[i - 1] * 2, 0

        return sorted(nums, key=lambda x: not x)
        
# @lc code=end

