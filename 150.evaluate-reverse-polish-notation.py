#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (33.01%)
# Likes:    662
# Dislikes: 390
# Total Accepted:    185.2K
# Total Submissions: 549.5K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#

# @lc code=start
from operator import truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for t in tokens:
            if not t in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a+b)
                elif t == '-':
                    stack.append(b-a)
                elif t == '*':
                    stack.append(a*b)
                elif t == '/':
                    stack.append(int(truediv(b, a)))

        return stack.pop()


        
# @lc code=end

