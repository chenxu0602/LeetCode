#
# @lc app=leetcode id=2567 lang=python3
#
# [2567] Minimum Score by Changing Two Elements
#

# @lc code=start
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
        
# @lc code=end

