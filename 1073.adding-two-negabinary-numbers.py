#
# @lc app=leetcode id=1073 lang=python3
#
# [1073] Adding Two Negabinary Numbers
#
# https://leetcode.com/problems/adding-two-negabinary-numbers/description/
#
# algorithms
# Medium (31.65%)
# Likes:    62
# Dislikes: 34
# Total Accepted:    4.1K
# Total Submissions: 12.9K
# Testcase Example:  '[1,1,1,1,1]\n[1,0,1]'
#
# Given two numbers arr1 and arr2 in base -2, return the result of adding them
# together.
# 
# Each number is given in array format:  as an array of 0s and 1s, from most
# significant bit to least significant bit.  For example, arr = [1,1,0,1]
# represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array
# format is also guaranteed to have no leading zeros: either arr == [0] or
# arr[0] == 1.
# 
# Return the result of adding arr1 and arr2 in the same format: as an array of
# 0s and 1s with no leading zeros.
# 
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# Explanation: arr1 represents 11, arr2 represents 5, the output represents
# 16.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= arr1.length <= 1000
# 1 <= arr2.length <= 1000
# arr1 and arr2 have no leading zeros
# arr1[i] is 0 or 1
# arr2[i] is 0 or 1
# 
#
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1, l2, sum_, ans = len(arr1), len(arr2), 0, []

        for i in range(1, max(l1, l2)+1):
            curr = [arr1[-i] if i <= l1 else None, arr2[-i] if i <= l2 else None]
            curr_1, curr_2 = [k * ((-2)**(i-1)) if k else 0 for k in curr]
            sum_ += curr_1 + curr_2

        while sum_:
            ans.append(sum_ % 2)
            sum_ = -(sum_ // 2)
        return ans[::-1] if ans else [0]
        

