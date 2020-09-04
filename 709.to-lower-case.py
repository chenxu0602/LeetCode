#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (77.11%)
# Likes:    310
# Dislikes: 1069
# Total Accepted:    130.7K
# Total Submissions: 168.9K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

        # is_upper = lambda x: 'A' <= x <= 'Z'
        # to_lower = lambda x: chr(ord(x) | 32)
        # return ''.join([to_lower(x) if is_upper(x) else x for x in str])
        

