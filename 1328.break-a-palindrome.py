#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#
# https://leetcode.com/problems/break-a-palindrome/description/
#
# algorithms
# Medium (44.88%)
# Likes:    188
# Dislikes: 192
# Total Accepted:    17.4K
# Total Submissions: 38.6K
# Testcase Example:  '"abccba"'
#
# Given a palindromic string palindrome, replace exactly one character by any
# lowercase English letter so that the string becomes the lexicographically
# smallest possible string that isn't a palindrome.
# 
# After doing so, return the final string.  If there is no way to do so, return
# the empty string.
# 
# 
# Example 1:
# 
# 
# Input: palindrome = "abccba"
# Output: "aaccba"
# 
# 
# Example 2:
# 
# 
# Input: palindrome = "a"
# Output: ""
# 
# 
# 
# Constraints:
# 
# 
# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''
        
# @lc code=end

