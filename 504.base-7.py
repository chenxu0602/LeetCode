#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (45.08%)
# Likes:    155
# Dislikes: 121
# Total Accepted:    43.2K
# Total Submissions: 95.9K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return '0'
        l, n = [], num < 0
        if n: num *= -1

        while num:
            l.append(str(num % 7))
            num //= 7

        if n: l.append('-')
        return ''.join(l[::-1])
        

