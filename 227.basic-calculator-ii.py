#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (34.18%)
# Likes:    898
# Dislikes: 161
# Total Accepted:    133.8K
# Total Submissions: 384.2K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#

# @lc code=start
from operator import truediv

class Solution:
    def calculate(self, s: str) -> int:

        s += '+0'
        stack, num, preOp = [], 0, '+'

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif not c.isspace():
                if preOp == '-':
                    stack.append(-num)
                elif preOp == '+':
                    stack.append(num)
                elif preOp == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(truediv(stack.pop(), num)))

                preOp, num = c, 0

        return int(sum(stack))

        
                



        
# @lc code=end

