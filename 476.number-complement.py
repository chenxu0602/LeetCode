#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.51%)
# Likes:    561
# Dislikes: 74
# Total Accepted:    110.2K
# Total Submissions: 176.3K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#
import math

class Solution:
    def findComplement(self, num: int) -> int:
        # n = floor(math.log2(num)) + 1
        # bitmask = (1 << n) - 1
        # return bitmask ^ num

        return num ^ (2 ** num.bit_length() - 1)
        

