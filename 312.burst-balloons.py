#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (49.82%)
# Likes:    1900
# Dislikes: 53
# Total Accepted:    83K
# Total Submissions: 166.5K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
# 
# Find the maximum coins you can collect by bursting the balloons wisely.
# 
# Note:
# 
# 
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# Example:
# 
# 
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1] + nums + [1]
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]

        # for gap in range(2, n):
        #     for i in range(n - gap):
        #         j = i + gap
        #         for k in range(i+1, j):
        #             dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])

        # return dp[0][n-1]


        # nums = [1] + nums + [1]
        # @lru_cache(None)
        # def dp(left, right):
        #     if left + 1 == right:
        #         return 0
        #     return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
        # return dp(0, len(nums)-1)

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                dp[left][right] = max(nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right))

        return dp[0][n-1]
        
# @lc code=end

