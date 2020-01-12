#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (58.09%)
# Likes:    316
# Dislikes: 72
# Total Accepted:    45K
# Total Submissions: 77.3K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits)-1))
        """

        n , cur = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True
        

