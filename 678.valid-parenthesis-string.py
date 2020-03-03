#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (32.98%)
# Likes:    724
# Dislikes: 26
# Total Accepted:    31.3K
# Total Submissions: 94.7K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].
# 
# 
#
class Solution:
    def checkValidString(self, s: str) -> bool:

        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0
        

