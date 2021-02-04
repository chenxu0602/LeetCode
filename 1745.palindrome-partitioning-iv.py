#
# @lc app=leetcode id=1745 lang=python3
#
# [1745] Palindrome Partitioning IV
#
# https://leetcode.com/problems/palindrome-partitioning-iv/description/
#
# algorithms
# Hard (48.42%)
# Likes:    147
# Dislikes: 2
# Total Accepted:    5.3K
# Total Submissions: 10.8K
# Testcase Example:  '"abcbdd"'
#
# Given a string s, return true if it is possible to split the string s into
# three non-empty palindromic substrings. Otherwise, return false.​​​​​
# 
# A string is said to be palindrome if it the same string when reversed.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcbdd"
# Output: true
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are
# palindromes.
# 
# 
# Example 2:
# 
# 
# Input: s = "bcbddxy"
# Output: false
# Explanation: s cannot be split into 3 palindromes.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 2000
# s​​​​​​ consists only of lowercase English letters.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # @lru_cache(None)
        # def helper(s, n):
        #     if n == 1: 
        #         return s == s[::-1]

        #     for i in range(len(s) - 1):
        #         if s[:i + 1] == s[:i + 1][::-1] and helper(s[i + 1:], n - 1):
        #             return True

        # return helper(s, 3)


        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

        for i in range(1, n):
            for j in range(i + 1, n):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][n - 1]:
                    return True

        return False

        
# @lc code=end

