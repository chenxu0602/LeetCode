#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.04%)
# Likes:    2513
# Dislikes: 76
# Total Accepted:    323.3K
# Total Submissions: 787.9K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp = [0] * (len(nums) + 2)
        # for i, num in enumerate(nums, 2):
        #     dp[i] = max(dp[i-2] + num, dp[i-1])
        # return dp[-1]

        prevMax = currMax = 0
        for i in nums:
            temp = currMax
            currMax = max(prevMax + i, currMax)
            prevMax = temp
        return currMax



        

