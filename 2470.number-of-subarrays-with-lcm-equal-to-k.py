#
# @lc app=leetcode id=2470 lang=python3
#
# [2470] Number of Subarrays With LCM Equal to K
#

# @lc code=start
import math

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:

        cnt = 0
        for i in range(len(nums)):
            l = nums[i]
            for j in range(i, len(nums)):
                l = math.lcm(l, nums[j])
                if l == k: cnt += 1
                if l > k: break

        return cnt
        
# @lc code=end

