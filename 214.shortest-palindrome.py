#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (28.86%)
# Likes:    902
# Dislikes: 103
# Total Accepted:    88.4K
# Total Submissions: 306K
# Testcase Example:  '"aacecaaa"'
#
# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.
# 
# Example 1:
# 
# 
# Input: "aacecaaa"
# Output: "aaacecaaa"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "dcbabcd"
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # i = 0
        # for j in range(len(s)-1, -1, -1):
        #     if s[i] == s[j]:
        #         i += 1
            
        # if i == len(s):
        #     return s

        # return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]

        r = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s
        
# @lc code=end

