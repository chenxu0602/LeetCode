#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (34.01%)
# Likes:    2095
# Dislikes: 98
# Total Accepted:    362K
# Total Submissions: 1.1M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # i, j = bisect_left(nums, target), bisect_right(nums, target)
        # if i == j:
        #     return [-1, -1]
        # return [i, j-1]

        def extrem_insertion_index(nums, target, left):
            lo, hi = 0, len(nums)
            while lo < hi:
                mi = lo + (hi - lo) // 2
                if nums[mi] > target or (left and target == nums[mi]):
                    hi = mi
                else:
                    lo = mi + 1
            return lo

        left_idx = extrem_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, extrem_insertion_index(nums, target, False)-1]


        
# @lc code=end

