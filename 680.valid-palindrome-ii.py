#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (34.45%)
# Likes:    813
# Dislikes: 54
# Total Accepted:    82.7K
# Total Submissions: 239.3K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution:
    def validPalindrome(self, s: str) -> bool:

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                t, u = s[:i] + s[i+1:], s[:-1-i] + s[len(s)-i:]
                return t == t[::-1] or u == u[::-1]
        return True
        

