#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (40.87%)
# Likes:    2523
# Dislikes: 58
# Total Accepted:    225.5K
# Total Submissions: 551.6K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        n = len(nums)
        if n == 0: return 0
        dp = [0] * n
        dp[0] = 1
        maxans = 1
        for i in range(n):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans
        """

        lst = []
        for num in nums:
            i = bisect.bisect_left(lst, num)
            if i >= len(lst):
                lst.append(num)
            lst[i] = num
        return len(lst)


        

