#
# @lc app=leetcode id=2831 lang=python3
#
# [2831] Find the Longest Equal Subarray
#

# @lc code=start
from collections import Counter

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:

        mx, l, count = 0, 0, Counter()
        for r, num in enumerate(nums):
            count[num] += 1
            mx = max(mx, count[num])

            if mx + k <= r - l:
                count[nums[l]] -= 1
                l += 1

        return mx
        
# @lc code=end

