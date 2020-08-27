#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.com/problems/strange-printer/description/
#
# algorithms
# Hard (37.14%)
# Likes:    273
# Dislikes: 36
# Total Accepted:    9.7K
# Total Submissions: 26.2K
# Testcase Example:  '"aaabbb"'
#
# 
# There is a strange printer with the following two special requirements:
# 
# 
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any places, and will cover the original existing characters.
# 
# 
# 
# 
# 
# Given a string consists of lower English letters only, your job is to count
# the minimum number of turns the printer needed in order to print it.
# 
# 
# Example 1:
# 
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
# 
# 
# 
# Hint: Length of the given string will not exceed 100.
#
from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        # memo = {}
        # def dfs(i, j):
        #     if i > j: return 0
        #     if (i, j) not in memo:
        #         ans = dfs(i+1, j) + 1
        #         for k in range(i+1, j+1):
        #             if s[k] == s[i]:
        #                 ans = min(ans, dfs(i, k-1) + dfs(k+1, j))
        #         memo[i, j] = ans
        #     return memo[i, j]

        # return dfs(0, len(s)-1)


        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            ans = dp(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
            return ans

        return dp(0, len(s) - 1)
        

