#
# @lc app=leetcode id=2411 lang=python3
#
# [2411] Smallest Subarrays With Maximum Bitwise OR
#

# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        last = [0] * 32
        n = len(nums)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            res[i] = max(1, max(last) - i + 1)

        return res
        
# @lc code=end

