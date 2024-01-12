#
# @lc app=leetcode id=2972 lang=python3
#
# [2972] Count the Number of Incremovable Subarrays II
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        nums = [0] + nums + [float('inf')]
        n = len(nums)
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                break
        else:
            return (n - 2) * (n - 1) // 2

        for j in range(n - 1, 0, -1):
            if nums[j - 1] >= nums[j]:
                break

        l, r = 0, j
        res = 0
        while l <= i:
            while r < n and nums[l] >= nums[r]:
                r += 1
            res += n - r
            l += 1

        return res

        
# @lc code=end

