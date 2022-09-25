#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True
            seen.add(s)
        return False
        
# @lc code=end

