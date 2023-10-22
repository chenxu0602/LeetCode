#
# @lc app=leetcode id=2770 lang=python3
#
# [2770] Maximum Number of Jumps to Reach the Last Index
#

# @lc code=start
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        n = len(nums)
        dp = [-1] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if -target <= nums[i] - nums[j] <= target and dp[j] != -1:
                    dp[i] = max(dp[i], 1 + dp[j]) 

        return dp[i]
        
# @lc code=end

