#
# @lc app=leetcode id=2765 lang=python3
#
# [2765] Longest Alternating Subarray
#

# @lc code=start
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        res = dp = -1
        for i in range(1, n):
            if dp > 0 and nums[i] == nums[i - 2]:
                dp += 1
            else:
                dp = 2 if nums[i] == nums[i - 1] + 1 else -1

            res = max(res, dp)

        return res 
    
        
# @lc code=end

