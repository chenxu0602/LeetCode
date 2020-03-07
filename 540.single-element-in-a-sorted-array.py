#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.48%)
# Likes:    777
# Dislikes: 62
# Total Accepted:    58.6K
# Total Submissions: 101.8K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# Given a sorted array consisting of only integers where every element appears
# exactly twice except for one element which appears exactly once. Find this
# single element that appears only once.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
#
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 0:
                mid += 1

            if nums[mid] == nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1

        return nums[low]


        

