#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (63.14%)
# Likes:    153
# Dislikes: 132
# Total Accepted:    27K
# Total Submissions: 42.8K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,2,3,1]
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 
#
import random 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)

    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.quicksort(lt) + eq + self.quicksort(gt)
        

