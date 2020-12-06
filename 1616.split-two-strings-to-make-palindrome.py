#
# @lc app=leetcode id=1616 lang=python3
#
# [1616] Split Two Strings to Make Palindrome
#
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/description/
#
# algorithms
# Medium (36.43%)
# Likes:    210
# Dislikes: 129
# Total Accepted:    10.1K
# Total Submissions: 27.7K
# Testcase Example:  '"x"\n"y"'
#
# You are given two strings a and b of the same length. Choose an index and
# split both strings at the same index, splitting a into two strings: aprefix
# and asuffix where a = aprefix + asuffix, and splitting b into two strings:
# bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix
# or bprefix + asuffix forms a palindrome.
# 
# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix
# is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" +
# "bc", "ab" + "c" , and "abc" + "" are valid splits.
# 
# Return true if it is possible to form a palindrome string, otherwise return
# false.
# 
# Notice that x + y denotes the concatenation of strings x and y.
# 
# 
# Example 1:
# 
# 
# Input: a = "x", b = "y"
# Output: true
# Explaination: If either a or b are palindromes the answer is true since you
# can split in the following way:
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
# 
# 
# Example 2:
# 
# 
# Input: a = "abdef", b = "fecab"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: a = "ulacfd", b = "jizalu"
# Output: true
# Explaination: Split them at index 3:
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
# 
# 
# Example 4:
# 
# 
# Input: a = "xbdef", b = "xecab"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^5
# a.length == b.length
# a and b consist of lowercase English letters
# 
# 
#

# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s, i, j):
            while i < j and s[i] == s[j]:
                i += 1; j -= 1
            return i >= j

        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1; j -= 1
            return isPalindrome(a, i, j) or isPalindrome(b, i, j)

        return check(a, b) or check(b, a)
        
# @lc code=end

