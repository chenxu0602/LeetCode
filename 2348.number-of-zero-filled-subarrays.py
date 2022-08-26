#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for num in nums:
            if num:
                count = 0
            else:
                count += 1

            ans += count
        return ans

        
# @lc code=end

