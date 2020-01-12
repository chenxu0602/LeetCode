#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (35.06%)
# Likes:    630
# Dislikes: 77
# Total Accepted:    141.8K
# Total Submissions: 404.4K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        s = pattern 
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))
        """

        f = lambda s: map({}.setdefault, s, range(len(s)))
        return list(f(pattern)) == list(f(str.split()))




