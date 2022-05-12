#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (50.22%)
# Likes:    1537
# Dislikes: 1905
# Total Accepted:    416K
# Total Submissions: 818.6K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Because we know that nums contains n numbers and that it is missing exactly one number on the range [0..n-1][0..n−1], we know that n definitely replaces the missing number in nums. Therefore, if we initialize an integer to n and XOR it with every index and value, we will be left with the missing number. 
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        
# @lc code=end

