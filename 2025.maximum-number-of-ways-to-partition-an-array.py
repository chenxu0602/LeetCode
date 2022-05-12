#
# @lc app=leetcode id=2025 lang=python3
#
# [2025] Maximum Number of Ways to Partition an Array
#

# @lc code=start
from collections import defaultdict

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:

        sum_ = sum(nums)
        n = len(nums)

        R, L = defaultdict(int), defaultdict(int)
        left = 0
        for i in range(n - 1):
            left += nums[i]
            right = sum_ - left
            R[left - right] += 1

        ans = R[0] # If we don't do any replacement, answer is the number of 0s in the frequency map
        left = 0
        for i in range(n):
            left += nums[i]
            right = sum_ - left

            d = k - nums[i]
            ans = max(ans, L[d] + R[-d])
            # transfer the frequency from R to L
            R[left - right] -= 1
            L[left - right] += 1

        return ans

        
# @lc code=end

