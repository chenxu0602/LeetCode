#
# @lc app=leetcode id=2202 lang=python3
#
# [2202] Maximize the Topmost Element After K Moves
#

# @lc code=start
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:

        if (len(nums) == 1) and (k & 1): return -1

        maxi = -1
        for i in range(min(len(nums), k - 1)):
            maxi = max(maxi, nums[i])

        if k < len(nums):
            maxi = max(maxi, nums[k])

        return maxi
        
# @lc code=end

