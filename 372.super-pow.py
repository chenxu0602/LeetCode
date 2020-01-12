#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.65%)
# Likes:    127
# Dislikes: 563
# Total Accepted:    28K
# Total Submissions: 78.5K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
# 
# Example 1:
# 
# 
# 
# Input: a = 2, b = [3]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# 
# 
#
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

#        (a**10)**b = a**(10*b)

        """
        result = 1
        for digit in b:
            result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
        return result
        """

        return pow(a, b.pop(), 1337) * pow(self.superPow(a, b), 10, 1337) % 1337 if b else 1

        """
        result = 1
        apower = a
        for digit in reversed(b):
            result = result * pow(apower, digit, 1337) % 1337
            apower = pow(apower, 10, 1337)

        return result
        """
        

