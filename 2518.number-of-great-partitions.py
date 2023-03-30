#
# @lc app=leetcode id=2518 lang=python3
#
# [2518] Number of Great Partitions
#

# @lc code=start
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        # Knapsack problem
        # which indicates the number of cases that we have a group with size i.
        if sum(nums) < k * 2: 
            return 0

        MOD = 10**9 + 7
        dp = [1] + [0] * (k - 1)
        for x in nums:
            for i in range(k - 1 - x, -1, -1):
                dp[i + x] += dp[i]

        return (pow(2, len(nums), MOD) - sum(dp) * 2) % MOD
        
# @lc code=end

