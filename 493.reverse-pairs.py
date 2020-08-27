#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (23.38%)
# Likes:    544
# Dislikes: 82
# Total Accepted:    25.9K
# Total Submissions: 110.6K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
# 
# You need to return the number of important reverse pairs in the given array.
# 
# Example1:
# 
# Input: [1,3,2,3,1]
# Output: 2
# 
# 
# Example2:
# 
# Input: [2,4,3,5,1]
# Output: 3
# 
# 
# Note:
# 
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# 
# 
#
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        s = []
        count = 0
        for i in reversed(range(len(nums))):
            count += bisect.bisect_left(s, nums[i])
            bisect.insort_left(s, nums[i] * 2)
        return count
        

