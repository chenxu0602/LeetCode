#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#
# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (47.24%)
# Likes:    123
# Dislikes: 238
# Total Accepted:    13.6K
# Total Submissions: 28.7K
# Testcase Example:  '"-1/2+1/2"'
#
# Given a string representing an expression of fraction addition and
# subtraction, you need to return the calculation result in string format. The
# final result should be irreducible fraction. If your final result is an
# integer, say 2, you need to change it to the format of fraction that has
# denominator 1. So in this case, 2 should be converted to 2/1.
# 
# Example 1:
# 
# Input:"-1/2+1/2"
# Output: "0/1"
# 
# 
# 
# Example 2:
# 
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# 
# 
# 
# Example 3:
# 
# Input:"1/3-1/2"
# Output: "-1/6"
# 
# 
# 
# Example 4:
# 
# Input:"5/3+1/3"
# Output: "2/1"
# 
# 
# 
# Note:
# 
# The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
# Each fraction (input and output) has format ±numerator/denominator. If the
# first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1,10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction
# format defined above. 
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
# 
# 
#
from math import gcd
from fractions import Fraction 
import re
from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(x, y):
            lcm = (x*y) // gcd(x ,y)
            return lcm

        def lcmm(*args):
            return reduce(lcm, args)

        num, denom = [], []
        m = re.findall("(([+|-]?\d+)/(\d+))", expression)
        for tup in m:
            num.append(int(tup[1].replace("+", "")))
            denom.append(int(tup[2]))

        mult = lcmm(*denom)
        sm = 0

        for i in range(len(denom)):
            num[i] *=  mult / denom[i]
            sm += num[i]

        frc = str(Fraction(int(sm), int(mult)))

        try:
            frc.index("/")
        except:
            frc += "/1"

        return frc

            
        

