#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#
# https://leetcode.com/problems/word-pattern-ii/description/
#
# algorithms
# Hard (40.95%)
# Likes:    254
# Dislikes: 18
# Total Accepted:    33.3K
# Total Submissions: 81.2K
# Testcase Example:  '"abab"\n"redblueredblue"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty substring in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# 
# Example 2:
# 
# 
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# 
# Example 3:
# 
# 
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
# 
# 
# Notes:
# You may assume both pattern and str contains only lowercase letters.
# 
#
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, str, dic):
        if len(pattern) == 0 and len(str) > 0:
            return False

        if len(pattern) == len(str) == 0:
            return True

        for end in range(1, len(str) - len(pattern) + 2):
            if pattern[0] not in dic and str[:end] not in dic.values():
                dic[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dic):
                    return True
                del dic[pattern[0]]
            elif pattern[0] in dic and dic[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dic):
                    return True

        return False



