#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.91%)
# Likes:    778
# Dislikes: 1365
# Total Accepted:    137K
# Total Submissions: 269.3K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
class Solution:
    def getSum(self, a: int, b: int) -> int:

        """
        def add(a, b):
            for _ in range(32):
                a, b = a ^ b, (a & b) << 1

            return a

        s = add(a, b) & 0xFFFFFFFF

        if s & 0x80000000:
            return -add(~(s & 0x7FFFFFFF) & 0x7FFFFFFF, 1)

        return s
        """

        while b != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        return a

#        a ^ b is add without counting the carry
#        a & b is carry part
        

