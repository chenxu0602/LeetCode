#
# @lc app=leetcode id=2919 lang=python3
#
# [2919] Minimum Increment Operations to Make Array Beautiful
#

# @lc code=start
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:

        # dp1 means to increment A[i - 3]
        # dp2 means to increment A[i - 2]
        # dp3 means to increment A[i - 1]
        dp1 = dp2 = dp3 = 0
        for num in nums:
            dp1, dp2, dp3 = dp2, dp3, min(dp1, dp2, dp3) + max(k - num, 0)

        return min(dp1, dp2, dp3)
        
# @lc code=end

