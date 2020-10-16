#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (53.13%)
# Likes:    568
# Dislikes: 140
# Total Accepted:    33.8K
# Total Submissions: 65K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (t concatenated with itself 1 or more times)
# 
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
# 
# 
# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Example 4:
# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""
# 
# 
# Constraints:
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
# 
# 
#

# @lc code=start
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # divisor = str1[:math.gcd(len(str1), len(str2))]

        # if all(s == len(s) // len(divisor) * divisor for s in (str1, str2)):
        #     return divisor

        # return ""


        n1, n2 = len(str1), len(str2)

        if n2 > n1:
            return self.gcdOfStrings(str2, str1)

        if str1[:n2] == str2:

            if n1 == n2:
                return str2

            return self.gcdOfStrings(str1[n2:], str2)

        return ""
        
# @lc code=end

