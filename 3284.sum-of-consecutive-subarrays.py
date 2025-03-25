#
# @lc app=leetcode id=3284 lang=python3
#
# [3284] Sum of Consecutive Subarrays
#

# @lc code=start
class Solution:
    def getSum(self, nums: List[int]) -> int:

        ans, MOD = nums[0], 10**9 + 7
        curr = nums[0]
        left, prior = 0, 0
        n = len(nums)

        for right in range(1, n):
            diff = nums[right] - nums[right - 1]

            if abs(diff) != 1:
                prior, left, curr = 0, right, 0
            elif prior != diff:
                prior, left, curr = diff, right - 1, nums[right - 1]

            curr += nums[right] * (right - left + 1)
            ans = (ans + curr) % MOD

        return ans

        
# @lc code=end

