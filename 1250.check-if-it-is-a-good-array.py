#
# @lc app=leetcode id=1250 lang=python3
#
# [1250] Check If It Is a Good Array
#
# https://leetcode.com/problems/check-if-it-is-a-good-array/description/
#
# algorithms
# Hard (51.94%)
# Likes:    55
# Dislikes: 134
# Total Accepted:    4.4K
# Total Submissions: 8.4K
# Testcase Example:  '[12,5,7,23]'
#
# Given an array nums of positive integers. Your task is to select some subset
# of nums, multiply each element by an integer and add all these numbers. The
# array is said to be good if you can obtain a sum of 1 from the array by any
# possible subset and multiplicand.
# 
# Return True if the array is good otherwise return False.
# 
# 
# Example 1:
# 
# 
# Input: nums = [12,5,7,23]
# Output: true
# Explanation: Pick numbers 5 and 7.
# 5*3 + 7*(-2) = 1
# 
# 
# Example 2:
# 
# 
# Input: nums = [29,6,10]
# Output: true
# Explanation: Pick numbers 29, 6 and 10.
# 29*1 + 6*(-3) + 10*(-1) = 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,6]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
from math import gcd
from functools import reduce

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return True if reduce(gcd, nums) == 1 else False

        # gcd = nums[0]
        # for a in nums:
        #     while a:
        #         gcd, a = a, gcd % a
        # return gcd == 1
        
# @lc code=end

