#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]):
            return 'none'

        if nums[0] == nums[1] == nums[2]:
            return 'equilateral'
        elif nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
            return 'scalene'
        
        return 'isosceles'
        

        
# @lc code=end

