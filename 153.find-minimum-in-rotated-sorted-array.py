#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.40%)
# Likes:    1282
# Dislikes: 184
# Total Accepted:    332.5K
# Total Submissions: 760.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#

# @lc code=start
from bisect import bisect_left, bisect

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # self.__getitem__ = lambda i: nums[i] <= nums[-1]
        # return nums[bisect(self, False, 0, len(nums))]

        # Binary Search
        # Time  complexity: O(logN)
        # Space complexity: O(1)
        # if len(nums) == 1:
        #     return nums[0]

        # left, right = 0, len(nums) - 1

        # if nums[left] < nums[right]:
        #     return nums[left]

        # while left <= right:
        #     mid = left + (right - left) // 2
            
        #     if nums[mid] > nums[mid + 1]:
        #         return nums[mid + 1]

        #     if nums[mid - 1] > nums[mid]:
        #         return nums[mid]

        #     if nums[mid] > nums[0]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1



        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
            

        
# @lc code=end

