#
# @lc app=leetcode id=3282 lang=python3
#
# [3282] Reach End of Array With Max Score
#

# @lc code=start
from itertools import accumulate

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        """
        n = len(nums)
        dp = [0] * n
        prefix = 0
        for i, v in enumerate(nums):
            if i:
                dp[i] = dp[i - 1] + prefix
            prefix = max(prefix, v)
        return dp[-1]
        """

        """
        ans = 0
        prev = nums.pop(0)
        for num in nums:
            ans += prev
            if num > prev:
                prev = num

        return ans
        """

        return sum(accumulate(nums[:-1], max))

        
# @lc code=end

