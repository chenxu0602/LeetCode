#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (42.48%)
# Likes:    757
# Dislikes: 43
# Total Accepted:    44.2K
# Total Submissions: 103.8K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#
import os, sys

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        """
        n = len(nums)
        sums = [0] * (n + 1)
        for i, v in enumerate(nums):
            sums[i+1] = sums[i] + nums[i]

        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min([max(dp[k][j-1], sums[i] - sums[k]) for k in range(i)])

        return dp[n][m]
        """

        n = len(nums)
        l, r = 0, 0

        for i in range(n):
            r += nums[i]
            if l < nums[i]:
                l = nums[i]

        ans = r
        while l <= r:
            mid = (l + r) >> 1
            s, cnt = 0, 1
            for i in range(n):
                if s + nums[i] > mid:
                    cnt += 1
                    s = nums[i]
                else:
                    s += nums[i]
            
            if cnt <= m:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans




