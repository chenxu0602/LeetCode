#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (29.53%)
# Likes:    90
# Dislikes: 439
# Total Accepted:    24.2K
# Total Submissions: 81.6K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
# 
# Given a non-empty string s and an abbreviation abbr, return whether the
# string matches with the given abbreviation.
# 
# 
# A string such as "word" contains only the following valid abbreviations:
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# Notice that only the above abbreviations are valid abbreviations of the
# string "word". Any other string is not a valid abbreviation of "word".
# 
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase
# letters and digits.
# 
# 
# Example 1:
# 
# Given s = "internationalization", abbr = "i12iz4n":
# 
# Return true.
# 
# 
# 
# Example 2:
# 
# Given s = "apple", abbr = "a2e":
# 
# Return false.
# 
# 
#
import re

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word)) 

        """
        if not word or not abbr:
            return False

        digits = [str(i) for i in range(10)]
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1; j += 1
                continue

            if not abbr[j].isdigit() or abbr[j] == '0':
                return False

            digits_start = j
            while j < len(abbr) and abbr[j].isdigit():
                j += 1

            i += int(abbr[digits_start:j])

        return i == len(word) and j == len(abbr)
        """


