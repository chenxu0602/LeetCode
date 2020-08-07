#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.29%)
# Likes:    869
# Dislikes: 30
# Total Accepted:    116.4K
# Total Submissions: 329.9K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#
class Solution:
    # Time  complexity: O(N)
    # Space complexity: O(1)
    def robline(self, nums: List[int]) -> int:
        prevMax = currMax = 0
        for i in nums:
            temp = currMax
            currMax = max(prevMax + i, currMax)
            prevMax = temp
        return currMax

    # def robline(self, nums: List[int]) -> int:
    #     dp = [0] * (len(nums) + 2)
    #     for i, num in enumerate(nums, 2):
    #         dp[i] = max(dp[i-1], dp[i-2] + num)

    #     return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        return max(map(self.robline, (nums[1:], nums[:-1])))        

