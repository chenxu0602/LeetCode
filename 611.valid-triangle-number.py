#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (45.57%)
# Likes:    625
# Dislikes: 75
# Total Accepted:    40.4K
# Total Submissions: 88.3K
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# 
# Note:
# 
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# 
# 
# 
#
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        c = 0
        nums.sort()
        n = len(nums)

        for i in range(n-1, -1, -1):
            low, high = 0, i - 1
            while low < high:
                if nums[high] + nums[low] > nums[i]:
                    c += high - low
                    high -= 1
                else:
                    low += 1

        return c   
        

