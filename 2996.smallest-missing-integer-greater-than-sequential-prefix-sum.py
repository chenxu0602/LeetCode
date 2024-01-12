#
# @lc app=leetcode id=2996 lang=python3
#
# [2996] Smallest Missing Integer Greater Than Sequential Prefix Sum
#

# @lc code=start
class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        count = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += nums[i]
            else:
                break

        while True:
            if count not in nums:
                return count
            else:
                count += 1
        
# @lc code=end

