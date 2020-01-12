#
# @lc app=leetcode id=1085 lang=python3
#
# [1085] Sum of Digits in the Minimum Number
#
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/description/
#
# algorithms
# Easy (73.71%)
# Likes:    11
# Dislikes: 43
# Total Accepted:    5.7K
# Total Submissions: 7.7K
# Testcase Example:  '[34,23,1,24,75,33,54,8]'
#
# Given an array A of positive integers, let S be the sum of the digits of the
# minimal element of A.
# 
# Return 0 if S is odd, otherwise return 1.
# 
# 
# 
# Example 1:
# 
# 
# Input: [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: 
# The minimal element is 1, and the sum of those digits is S = 1 which is odd,
# so the answer is 0.
# 
# 
# Example 2:
# 
# 
# Input: [99,77,33,66,55]
# Output: 1
# Explanation: 
# The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which
# is even, so the answer is 1.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# 
#
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 - sum(map(int, str(min(A)))) % 2
        

