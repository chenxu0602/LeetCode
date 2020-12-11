#
# @lc app=leetcode id=1682 lang=python3
#
# [1682] Longest Palindromic Subsequence II
#
# https://leetcode.com/problems/longest-palindromic-subsequence-ii/description/
#
# algorithms
# Medium (44.59%)
# Likes:    12
# Dislikes: 5
# Total Accepted:    221
# Total Submissions: 456
# Testcase Example:  '"bbabab"'
#
# A subsequence of a string s is considered a good palindromic subsequence
# if:
# 
# 
# It is a subsequence of s.
# It is a palindrome (has the same value if reversed).
# It has an even length.
# No two consecutive characters are equal, except the two middle ones.
# 
# 
# For example, if s = "abcabcabb", then "abba" is considered a good palindromic
# subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive
# characters) are not.
# 
# Given a string s, return the length of the longest good palindromic
# subsequence in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "bbabab"
# Output: 4
# Explanation: The longest good palindromic subsequence of s is "baab".
# 
# 
# Example 2:
# 
# 
# Input: s = "dcbccacdb"
# Output: 4
# Explanation: The longest good palindromic subsequence of s is "dccd".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 250
# s consists of lowercase English letters.
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # O(N^2)

        @lru_cache(None)
        def dp(l, r, prev):
            if l >= r:
                return 0

            if s[l] == s[r] and s[l] != prev:
                return 2 + dp(l + 1, r - 1, s[l])

            return max(dp(l + 1, r, prev), dp(l, r - 1, prev))

        res = dp(0, len(s) - 1, "")
        dp.cache_clear()
        return res
        
# @lc code=end

