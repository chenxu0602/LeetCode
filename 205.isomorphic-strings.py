#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (37.90%)
# Likes:    927
# Dislikes: 271
# Total Accepted:    236.5K
# Total Submissions: 615.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        """
        if not len(s) == len(t):
            return False

        n = len(s)

        m1, m2 = defaultdict(int), defaultdict(int)

        for i in range(n):
            if not m1[s[i]] == m2[t[i]]:
                return False

            m1[s[i]] = i + 1
            m2[t[i]] = i + 1

        return True
        """

        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        """

        """
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        """

        """
        return list(map(s.find, s)) == list(map(t.find, t))
        """

        
# @lc code=end

