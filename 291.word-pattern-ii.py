#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#
# https://leetcode.com/problems/word-pattern-ii/description/
#
# algorithms
# Hard (42.70%)
# Likes:    376
# Dislikes: 24
# Total Accepted:    40.9K
# Total Submissions: 95.9K
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

# @lc code=start
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:

        # O(C(k - 1, t - 1))
        # t = len(pattern), k = len(str)
        def dfs(pattern, s, dic):
            if len(pattern) == 0 and len(s) > 0:
                return False
            
            if len(pattern) == len(s) == 0:
                return True

            for end in range(1, len(s) - len(pattern) + 2):
                if pattern[0] not in dic and s[:end] not in dic.values():
                    dic[pattern[0]] = s[:end]
                    if dfs(pattern[1:], s[end:], dic):
                        return True
                    del dic[pattern[0]]
                elif pattern[0] in dic and dic[pattern[0]] == s[:end]:
                    if dfs(pattern[1:], s[end:], dic):
                        return True

            return False

        return dfs(pattern, str, {})

        
# @lc code=end

