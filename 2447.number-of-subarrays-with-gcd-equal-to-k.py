#
# @lc app=leetcode id=2447 lang=python3
#
# [2447] Number of Subarrays With GCD Equal to K
#

# @lc code=start
import math 

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        count = 0
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = math.gcd(g, nums[j])

                if g == k: count += 1

                if g < k: break

        return count
        
# @lc code=end

