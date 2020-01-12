#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#
# https://leetcode.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (65.79%)
# Likes:    169
# Dislikes: 585
# Total Accepted:    38K
# Total Submissions: 57.7K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 
# Given two strings representing two complex numbers.
# 
# 
# You need to return a string representing their multiplication. Note i^2 = -1
# according to the definition.
# 
# 
# Example 1:
# 
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i, and you need convert
# it to the form of 0+2i.
# 
# 
# 
# Example 2:
# 
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i, and you need convert
# it to the form of 0+-2i.
# 
# 
# 
# Note:
# 
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and
# b will both belong to the range of [-100, 100]. And the output should be also
# in this form.
# 
# 
#
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, _, a = a.partition('+')
        a2, _, _ = a.partition('i')
        b1, _, b = b.partition('+')
        b2, _, _ = b.partition('i')

        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        result = [str(a1*b1-a2*b2), '+', str(a1*b2+a2*b1), 'i']

        return ''.join(result)
        

