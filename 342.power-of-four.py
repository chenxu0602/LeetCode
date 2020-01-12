#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (40.29%)
# Likes:    317
# Dislikes: 145
# Total Accepted:    115.3K
# Total Submissions: 285.7K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
#        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0
#        return num > 0 and num & (num - 1) == 0 and len(bin(num)[3:]) % 2 == 0
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
        

