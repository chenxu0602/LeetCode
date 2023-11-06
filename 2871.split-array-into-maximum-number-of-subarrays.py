#
# @lc app=leetcode id=2871 lang=python3
#
# [2871] Split Array Into Maximum Number of Subarrays
#

# @lc code=start
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        # If the score of A is x, then the score of each subarray of A bigger or equal to x.
        # If x > 0, 2x > x, so we won't split A, return 1.
        # If x == 0, so we may split A, into multiple subarray with score 0.

        v = -1
        res = 0
        for num in nums:
            v &= num
            if v == 0:
                v = -1; res += 1

        return max(1, res)
        
# @lc code=end

