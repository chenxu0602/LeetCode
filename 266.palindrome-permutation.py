#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (60.10%)
# Likes:    198
# Dislikes: 40
# Total Accepted:    66.8K
# Total Submissions: 111.1K
# Testcase Example:  '"code"'
#
# Given a string, determine if a permutation of the string could form a
# palindrome.
# 
# Example 1:
# 
# 
# Input: "code"
# Output: false
# 
# Example 2:
# 
# 
# Input: "aab"
# Output: true
# 
# Example 3:
# 
# 
# Input: "carerac"
# Output: true
# 
#

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return [n & 1 for n in Counter(s).values()].count(1) < 2

