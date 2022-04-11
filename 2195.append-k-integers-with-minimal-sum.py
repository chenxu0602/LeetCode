#
# @lc app=leetcode id=2195 lang=python3
#
# [2195] Append K Integers With Minimal Sum
#

# @lc code=start
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        nums = sorted(list(set(nums)))
        n = len(nums)

        if nums[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] - mid <= k:
                left = mid + 1
            else:
                right = mid

        return (k + left) * (k + left + 1) // 2 - sum(nums[:left])
        
# @lc code=end

