#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#

# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        # n = len(nums)
        # dp = [[-1] * (target + 1) for _ in range(n + 1)]

        # for i in range(n + 1):
        #     dp[i][0] = 0

        # for i in range(1, n + 1):
        #     for j in range(1, target + 1):
        #         dp[i][j] = dp[i - 1][j]
        #         if j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]] != -1:
        #             dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j - nums[i - 1]])

        # return dp[n][target]



        dp = [float("-inf")] * (target + 1)
        dp[0] = 0
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + 1)

        return dp[target] if dp[target] != float("-inf") else -1
        
# @lc code=end

