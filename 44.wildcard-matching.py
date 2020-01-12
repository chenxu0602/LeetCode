#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (23.21%)
# Likes:    1344
# Dislikes: 80
# Total Accepted:    200.1K
# Total Submissions: 851.3K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        n = len(s)
        if len(p) - p.count('*') > n:
            return False

        dp = [True] + [False] * n
        for i in p:
            if i != '*':
                for j in reversed(range(n)):
                    dp[j+1] = dp[j] and (i == s[j] or i == '?')
            else:
                for j in range(1, n+1):
                    dp[j] = dp[j-1] or dp[j]

            dp[0] = dp[0] and i == '*'
        return dp[-1]
        """

        """
        def remove_duplicate_stars(p):
            if p == "":
                return p
            p1 = [p[0],]
            for x in p[1:]:
                if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                    p1.append(x)
            return "".join(p1)

        @lru_cache(None)
        def helper(s, p):
            if p == s or p == '*':
                return True
            elif p == "" or s == "":
                return False
            elif p[0] == s[0] or p[0] == '?':
                return helper(s[1:], p[1:])
            elif p[0] == '*':
                return helper(s, p[1:]) or helper(s[1:], p)
            else:
                return False

        p = remove_duplicate_stars(p)
        return helper(s, p)
        """

        """
        s_len, p_len = len(s), len(p)

        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False

        d = [[False] * (s_len+1) for _ in range(p_len+1)]
        d[0][0] = True

        for p_idx in range(1, p_len+1):
            if p[p_idx-1] == '*':
                s_idx = 1
                while not d[p_idx-1][s_idx-1] and s_idx < s_len + 1:
                    s_idx += 1

                d[p_idx][s_idx-1] = d[p_idx-1][s_idx-1]

                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx-1] == '?':
                for s_idx in range(1, s_len+1):
                    d[p_idx][s_idx] = d[p_idx-1][s_idx-1]
            else:
                for s_idx in range(1, s_len+1):
                    d[p_idx][s_idx] = d[p_idx-1][s_idx-1] and p[p_idx-1] == s[s_idx-1]

        return d[p_len][s_len]
        """


        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        return all(x == '*' for x in p[p_idx:])



        
# @lc code=end

