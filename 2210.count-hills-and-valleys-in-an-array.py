#
# @lc app=leetcode id=2210 lang=python3
#
# [2210] Count Hills and Valleys in an Array
#

# @lc code=start
class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        hillValley = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]

            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                hillValley += 1

            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                hillValley += 1

        return hillValley

        
# @lc code=end

