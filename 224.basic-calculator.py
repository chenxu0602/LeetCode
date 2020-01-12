#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (33.59%)
# Likes:    960
# Dislikes: 105
# Total Accepted:    126.8K
# Total Submissions: 369.2K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:


        """
        def evaluate_expr(stack):
            res = stack.pop() if stack else 0
            while stack and stack[-1] != ')':
                sign = stack.pop()
                if sign == '+':
                    res += stack.pop()
                else:
                    res -= stack.pop()
            return res

        stack = []
        n, operand = 0, 0

        for i in range(len(s)-1, -1, -1):
            ch = s[i]

            if ch.isdigit():
                operand = (10**n * int(ch)) + operand
                n += 1
            elif ch != " ":
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':
                    res = evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
            
        if n:
            stack.append(operand)

        return evaluate_expr(stack)
        """

        stack, operand, res, sign = [], 0, 0, 1

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0

        return res + sign * operand



            
        
# @lc code=end

