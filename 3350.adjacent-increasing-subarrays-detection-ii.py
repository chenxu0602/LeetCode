#
# @lc app=leetcode id=3350 lang=python3
#
# [3350] Adjacent Increasing Subarrays Detection II
#

# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        up, pre_max_up = 1, 0
        res = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up += 1
            else:
                pre_max_up = up
                up = 1

            res = max(res, up // 2, min(pre_max_up, up))

        return res

        
# @lc code=end

