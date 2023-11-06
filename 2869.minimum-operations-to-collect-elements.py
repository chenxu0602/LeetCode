#
# @lc app=leetcode id=2869 lang=python3
#
# [2869] Minimum Operations to Collect Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n, mask = len(nums), 0
        for i in range(n):
            if nums[~i] <= k:
                mask |= 1 << nums[~i]

            if bin(mask).count('1') == k:
                break

        return i + 1
        
        
# @lc code=end

