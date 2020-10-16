#
# @lc app=leetcode id=1150 lang=python3
#
# [1150] Check If a Number Is Majority Element in a Sorted Array
#
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description/
#
# algorithms
# Easy (59.42%)
# Likes:    135
# Dislikes: 19
# Total Accepted:    14.9K
# Total Submissions: 25.4K
# Testcase Example:  '[2,4,5,5,5,5,5,6,6]\n5'
#
# Given an array nums sorted in non-decreasing order, and a number target,
# return True if and only if target is a majority element.
# 
# A majority element is an element that appears more than N/2 times in an array
# of length N.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: 
# The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: 
# The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^9
# 1 <= target <= 10^9
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if nums[len(nums) // 2] != target:
            return False

        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target) > len(nums) // 2
        
# @lc code=end

