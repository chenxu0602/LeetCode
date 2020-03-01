#
# @lc app=leetcode id=772 lang=python3
#
# [772] Basic Calculator III
#
# https://leetcode.com/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (40.78%)
# Likes:    374
# Dislikes: 144
# Total Accepted:    29.8K
# Total Submissions: 73.2K
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

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:

        num, stack, sign = 0, [], '+'
        s += ' '
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                num, skip = self.calculate(s[i+1:])
                i += skip
            elif s[i] in '+-*/)' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    last = stack.pop()
                    stack.append(last // num if last > 0 else -(-last // num))

                if s[i] == ')':
                    return sum(stack), i + 1

                num = 0
                sign = s[i]

            i += 1

        return sum(stack)
        
# @lc code=end

