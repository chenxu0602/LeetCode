#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (59.07%)
# Likes:    1971
# Dislikes: 96
# Total Accepted:    147.3K
# Total Submissions: 249.2K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        L, r = len(s), 0
        for i in range(L):
            for a, b in [(i, i), (i, i+1)]:
                while a >= 0 and b < L and s[a] == s[b]:
                    a -= 1; b += 1
                r += (b - a) // 2
        return r
        
# @lc code=end

