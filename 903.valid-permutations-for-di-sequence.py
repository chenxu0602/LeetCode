#
# @lc app=leetcode id=903 lang=python3
#
# [903] Valid Permutations for DI Sequence
#
# https://leetcode.com/problems/valid-permutations-for-di-sequence/description/
#
# algorithms
# Hard (45.55%)
# Likes:    200
# Dislikes: 25
# Total Accepted:    3.7K
# Total Submissions: 8.1K
# Testcase Example:  '"DID"'
#
# We are given S, a length n string of characters from the set {'D', 'I'}.
# (These letters stand for "decreasing" and "increasing".)
# 
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1,
# ..., n}, such that for all i:
# 
# 
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# 
# 
# How many valid permutations are there?  Since the answer may be large, return
# your answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "DID"
# Output: 5
# Explanation: 
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# S consists only of characters from the set {'D', 'I'}.
# 
# 
# 
# 
# 
# 
#
from functools import lru_cache

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)

        @lru_cache(None)
        def dp(i, j):
            if not 0 <= j <= i:
                return 0

            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return sum(dp(i-1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i-1, k) for k in range(j)) % MOD
        return sum(dp(N, j) for j in range(N+1)) % MOD
        

