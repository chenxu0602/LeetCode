#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.47%)
# Likes:    1144
# Dislikes: 251
# Total Accepted:    58.8K
# Total Submissions: 302.4K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2
            or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
        

