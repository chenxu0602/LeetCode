#
# @lc app=leetcode id=702 lang=python3
#
# [702] Search in a Sorted Array of Unknown Size
#
# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
#
# algorithms
# Medium (66.54%)
# Likes:    344
# Dislikes: 26
# Total Accepted:    28.9K
# Total Submissions: 43K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an integer array sorted in ascending order, write a function to search
# target in nums.  If target exists, then return its index, otherwise return
# -1. However, the array size is unknown to you. You may only access the array
# using an ArrayReader interface, where ArrayReader.get(k) returns the element
# of the array at index k (0-indexed).
# 
# You may assume all integers in the array are less than 10000, and if you
# access the array out of bounds, ArrayReader.get will return 2147483647.
# 
# 
# 
# Example 1:
# 
# 
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# You may assume that all elements in the array are unique.
# The value of each element in the array will be in the range [-9999,
# 9999].
# The length of the array will be in the range [1, 10^4].
# 
# 
#

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Time  complexity: O(logT), where T is an index of target value.
        # Space complexity: O(1)
        if reader.get(0) == target: return 0

        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            num = reader.get(mid)

            if num == target:
                return mid

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
        
# @lc code=end

