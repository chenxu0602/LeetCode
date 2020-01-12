#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (40.22%)
# Likes:    228
# Dislikes: 11
# Total Accepted:    7K
# Total Submissions: 17.4K
# Testcase Example:  '"abc"'
#
# Given a string S, count the number of distinct, non-empty subsequences of S
# .
# 
# Since the result may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
# 
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
# "aba".
# 
# 
# 
# Example 3:
# 
# 
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
# 
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
# S contains only lowercase letters.
# 1 <= S.length <= 2000
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
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp, MOD = [0] * len(S), 10**9 + 7
        for i, char in enumerate(S):
            ind = S.rfind(char, 0, i)
            dp[i] = 1 + sum(dp[:i]) % MOD if ind == -1 else sum(dp[ind:i]) % MOD
        return sum(dp) % MOD
        

