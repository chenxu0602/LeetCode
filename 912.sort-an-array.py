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
        # self.mergeSort(nums)
        self.quicksort_inplace(nums, 0, len(nums)-1)
        return nums

    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.quicksort(lt) + eq + self.quicksort(gt)

    def quicksort_inplace(self, nums, low, high):
        def partition(nums, low, high):
            i = low
            pivot = nums[high]
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        if low < high:
            pi = partition(nums, low, high)
            self.quicksort_inplace(nums, low, pi - 1)
            self.quicksort_inplace(nums, pi + 1, high)


    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]; R = nums[mid:]
            self.mergeSort(L); self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1; k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1; k += 1

        

