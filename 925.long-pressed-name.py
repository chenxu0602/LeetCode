#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.49%)
# Likes:    294
# Dislikes: 40
# Total Accepted:    21.9K
# Total Submissions: 49.2K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
from itertools import groupby

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        g1 = [(k, len(list(grp))) for k, grp in groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in groupby(typed)]

        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))
        """

        j = 0
        for c in name:
            if j == len(typed):
                return False

            if typed[j] != c:
                if (j == 0) or (typed[j-1] != typed[j]):
                    return False

                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j += 1

                if j == len(typed) or typed[j] != c:
                    return False

            j += 1

        return True
        

