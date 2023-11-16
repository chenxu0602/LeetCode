#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
#

# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n + 1):
                ans += len(set(nums[i:j])) ** 2

        return ans
        
# @lc code=end

