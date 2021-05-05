#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#
# https://leetcode.com/problems/replace-all-digits-with-characters/description/
#
# algorithms
# Easy (82.88%)
# Likes:    58
# Dislikes: 8
# Total Accepted:    7.9K
# Total Submissions: 9.6K
# Testcase Example:  '"a1c1e1"'
#
# You are given a 0-indexed string s that has lowercase English letters in its
# even indices and digits in its odd indices.
# 
# There is a function shift(c, x), where c is a character and x is a digit,
# that returns the x^th character after c.
# 
# 
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# 
# 
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1],
# s[i]).
# 
# Return s after replacing all digits. It is guaranteed that shift(s[i-1],
# s[i]) will never exceed 'z'.
# 
# 
# Example 1:
# 
# 
# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'
# 
# Example 2:
# 
# 
# Input: s = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# shift(s[i-1], s[i]) <= 'z' for all odd indices i.
# 
# 
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:

        s = list(s)
        for i, x in enumerate(s):
            if i % 2 == 1:
                s[i] = chr(ord(s[i - 1]) + int(x))

        return "".join(s)
        
# @lc code=end

