#
# @lc app=leetcode id=1243 lang=python3
#
# [1243] Array Transformation
#
# https://leetcode.com/problems/array-transformation/description/
#
# algorithms
# Easy (52.54%)
# Likes:    32
# Dislikes: 17
# Total Accepted:    4.3K
# Total Submissions: 8.2K
# Testcase Example:  '[6,2,3,4]\r'
#
# Given an initial array arr, every day you produce a new array using the array
# of the previous day.
# 
# On the i-th day, you do the following operations on the array of day i-1 to
# produce the array of day i:
# 
# 
# If an element is smaller than both its left neighbor and its right neighbor,
# then this element is incremented.
# If an element is bigger than both its left neighbor and its right neighbor,
# then this element is decremented.
# The first and last elements never change.
# 
# 
# After some days, the array does not change. Return that final array.
# 
# 
# Example 1:
# 
# 
# Input: arr = [6,2,3,4]
# Output: [6,3,3,4]
# Explanation: 
# On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
# No more operations can be done to this array.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,6,3,4,3,5]
# Output: [1,4,4,4,4,5]
# Explanation: 
# On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
# On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
# No more operations can be done to this array.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        change = True
        while change:
            new = arr[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(arr, arr[1:], arr[2:])] + arr[-1:]
            arr, change = new, arr != new
        return arr
        
# @lc code=end

