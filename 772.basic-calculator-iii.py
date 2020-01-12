#
# @lc app=leetcode id=772 lang=python3
#
# [772] Basic Calculator III
#
# https://leetcode.com/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (42.15%)
# Likes:    263
# Dislikes: 82
# Total Accepted:    19.6K
# Total Submissions: 46.7K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators , open ( and closing parentheses ) and empty spaces  . The integer
# division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2147483648, 2147483647].
# 
# Some examples:
# 
# 
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
#
import re

class Solution:
    def getSubExpr(self, s):
        left = 1
        x = []
        while left != 0:
            x.append(next(s))
            if x[-1] == '(':
                left += 1
            elif x[-1] == ')':
                left -= 1
        return ''.join(x[:-1])

    def calculate(self, s: str) -> int:
        """
        num, stack, sign = 0, [], '+'
        s += ' '
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num, skip = self.calculate(s[i+1:])
                i += skip
            elif s[i] in '+-*/)' or i== len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() // num))

                if s[i] == ')':
                    return sum(stack), i + 1
                num = 0
                sign = s[i]
            i += 1
        return sum(stack)
        """

        s = iter(re.findall('\d+|\S', s))
        operand, sign = 0, 1
        total = 0
        for token in s:
            if token in '+-':
                total += sign * operand
                sign = [1, -1][token == '-']
            elif token in '/*':
                n = next(s)
                n = self.calculate(self.getSubExpr(s)) if n == '(' else int(n)
                operand = operand * n if token == '*' else operand // n
            else:
                operand = self.calculate(self.getSubExpr(s)) if token == '(' else int(token)
        return total + sign * operand
            

        
