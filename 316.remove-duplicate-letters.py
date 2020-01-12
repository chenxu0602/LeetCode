#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (32.60%)
# Likes:    749
# Dislikes: 78
# Total Accepted:    57.8K
# Total Submissions: 176.7K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
#

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        """
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                print(result)
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result
        """

        """
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0: break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ""
        """

        """
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
        return ""
        """

        """
        result = ""
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[:i+1])
            result += c
            s = s[s.index(c):].replace(c, "")
        return result
        """

        rindex = {c: i for i, c in enumerate(s)}
        result = ""
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result



        

