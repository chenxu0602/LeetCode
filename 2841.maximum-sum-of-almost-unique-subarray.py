#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
from collections import Counter

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        count, sm = Counter(nums[:k]), sum(nums[:k])
        mx = sm if len(count) >= m else 0

        for right, left in zip(nums[k:], nums):
            count[right] += 1
            count[left]  -= 1
            sm += right - left

            if count[left] == 0: del count[left]
            if len(count) >= m: mx = max(mx, sm)

        return mx
        
# @lc code=end

