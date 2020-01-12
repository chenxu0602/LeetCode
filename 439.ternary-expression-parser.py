#
# @lc app=leetcode id=439 lang=python3
#
# [439] Ternary Expression Parser
#
# https://leetcode.com/problems/ternary-expression-parser/description/
#
# algorithms
# Medium (53.78%)
# Likes:    181
# Dislikes: 28
# Total Accepted:    15.4K
# Total Submissions: 28.6K
# Testcase Example:  '"T?2:3"'
#
# Given a string representing arbitrarily nested ternary expressions, calculate
# the result of the expression. You can always assume that the given expression
# is valid and only consists of digits 0-9, ?, :, T and F (T and F represent
# True and False respectively).
# 
# Note:
# 
# The length of the given string is ≤ 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never
# be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or
# F.
# 
# 
# 
# 
# Example 1:
# 
# Input: "T?2:3"
# 
# Output: "2"
# 
# Explanation: If true, then result is 2; otherwise result is 3.
# 
# 
# 
# 
# Example 2:
# 
# Input: "F?1:T?4:5"
# 
# Output: "4"
# 
# Explanation: The conditional expressions group right-to-left. Using
# parenthesis, it is read/evaluated as:
# 
# ⁠            "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 :
# 5))"
# ⁠         -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
# ⁠         -> "4"                                    -> "4"
# 
# 
# 
# 
# Example 3:
# 
# Input: "T?T?F:5:3"
# 
# Output: "F"
# 
# Explanation: The conditional expressions group right-to-left. Using
# parenthesis, it is read/evaluated as:
# 
# ⁠            "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) :
# 3)"
# ⁠         -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
# ⁠         -> "F"                                    -> "F"
# 
# 
#
class Solution:
    def parseTernary(self, expression: str) -> str:

        while not len(expression) == 1:
            i = expression.rindex('?') 
            tmp = expression[i+1] if expression[i-1] == 'T' else expression[i+3]
            expression = expression[:i-1] + tmp + expression[i+4:]
        return expression

    
        

