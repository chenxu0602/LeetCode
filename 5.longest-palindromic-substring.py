#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.74%)
# Likes:    4525
# Dislikes: 407
# Total Accepted:    681.2K
# Total Submissions: 2.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res 

        
# @lc code=end

