#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (46.80%)
# Likes:    228
# Dislikes: 64
# Total Accepted:    27.4K
# Total Submissions: 58.6K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# Given a sorted array of integers nums and integer values a, b and c. Apply a
# quadratic function of the form f(x) = ax^2 + bx + c to each element x in the
# array.
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]
# 
# 
# 
#
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def func(x):
            return a*x*x + b*x + c

        return sorted(map(func, nums))
        

