#
# @lc app=leetcode id=6909 lang=python3
#
# [6909] Longest Even Odd Subarray With Threshold
#

# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        ans, i, last, n = 0, 1, float("inf"), len(nums)

        if nums[0] <= threshold and nums[0] % 2 == 0:
            last = 0

        while i < n:
            if nums[i] > threshold or ((nums[i] % 2) == (nums[i - 1] % 2)):
                ans = max(ans, i - last)
                last = float("inf")

            if last == float("inf") and nums[i] <= threshold and nums[i] % 2 == 0:
                last = i

            i += 1

        ans = max(ans, i - last)
        return ans

        
# @lc code=end

