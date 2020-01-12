#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#
# https://leetcode.com/problems/solve-the-equation/description/
#
# algorithms
# Medium (40.49%)
# Likes:    172
# Dislikes: 411
# Total Accepted:    19K
# Total Submissions: 46.9K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# 
# Solve a given equation and return the value of x in the form of string
# "x=#value". The equation contains only '+', '-' operation, the variable x and
# its coefficient.
# 
# 
# 
# If there is no solution for the equation, return "No solution".
# 
# 
# If there are infinite solutions for the equation, return "Infinite
# solutions".
# 
# 
# If there is exactly one solution for the equation, we ensure that the value
# of x is an integer.
# 
# 
# Example 1:
# 
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# 
# 
# 
# Example 2:
# 
# Input: "x=x"
# Output: "Infinite solutions"
# 
# 
# 
# Example 3:
# 
# Input: "2x=x"
# Output: "x=0"
# 
# 
# 
# Example 4:
# 
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# 
# 
# 
# Example 5:
# 
# Input: "x=x+2"
# Output: "No solution"
# 
# 
#
class Solution:
    def solveEquation(self, equation: str) -> str:
        z = eval(equation.replace('x', 'j').replace('=', '-(') + ')', {'j': 1j})
        a, x = z.real, -z.imag
        return "x={}".format(int(a//x)) if x else "No solution" if a else "Infinite solutions"
        

