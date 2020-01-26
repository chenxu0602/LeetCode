#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#
# https://leetcode.com/problems/count-different-palindromic-subsequences/description/
#
# algorithms
# Hard (39.34%)
# Likes:    319
# Dislikes: 34
# Total Accepted:    9.5K
# Total Submissions: 24K
# Testcase Example:  '"bccb"'
#
# 
# Given a string S, find the number of different non-empty palindromic
# subsequences in S, and return that number modulo 10^9 + 7.
# 
# A subsequence of a string S is obtained by deleting 0 or more characters from
# S.
# 
# A sequence is palindromic if it is equal to the sequence reversed.
# 
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some
# i for which A_i != B_i.
# 
# 
# Example 1:
# 
# Input: 
# S = 'bccb'
# Output: 6
# Explanation: 
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc',
# 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# 
# 
# 
# Example 2:
# 
# Input: 
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation: 
# There are 3104860382 different non-empty palindromic subsequences, which is
# 104860361 modulo 10^9 + 7.
# 
# 
# 
# Note:
# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
# 
#
from functools import lru_cache

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:

        @lru_cache(None)
        def dfs(start, end):
            count = 0
            segment = S[start:end]

            if end <= start + 2:
                return end - start

            for x in "abcd":
                try:
                    i = segment.index(x) + start
                    j = segment.rindex(x) + start
                except:
                    continue

                count += dfs(i+1, j) + 2 if i != j else 1

            return count % (10**9 + 7)

        return dfs(0, len(S))
