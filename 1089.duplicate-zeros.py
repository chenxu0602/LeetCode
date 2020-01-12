#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (59.02%)
# Likes:    163
# Dislikes: 113
# Total Accepted:    20.1K
# Total Submissions: 34.1K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return
# anything from your function.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
# 
#
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        for left in range(length_ + 1):
            if left > length_ - possible_dups:
                break

            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1

        last = length_ - possible_dups

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+possible_dups] = 0
                possible_dups -= 1
                arr[i+possible_dups] = 0
            else:
                arr[i+possible_dups] = arr[i]
        

