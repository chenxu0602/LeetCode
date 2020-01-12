#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (75.15%)
# Likes:    227
# Dislikes: 336
# Total Accepted:    48.5K
# Total Submissions: 64.5K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string
# concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does
# not exist a way to split it into S = A+B, with A and B nonempty valid
# parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S =
# P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string
# in the primitive decomposition of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
# 
# 
# 
# Example 2:
# 
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        parts = []
        left_n, right_n = 0, 0

        j = 0
        for i in range(len(S)):
            if S[i] == '(':
                left_n += 1
            else:
                right_n += 1

            if left_n == right_n:
                parts.append(S[j+1:i])
                j = i + 1

        return "".join(parts)
        

