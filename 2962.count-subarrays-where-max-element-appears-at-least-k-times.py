#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        ma = max(nums)
        res = cur = i = 0
        for j in range(len(nums)):
            cur += nums[j] == ma
            while cur >= k:
                cur -= nums[i] == ma
                i += 1
            res += i

        return res
        
# @lc code=end

