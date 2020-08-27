#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#
# https://leetcode.com/problems/decode-ways-ii/description/
#
# algorithms
# Hard (25.36%)
# Likes:    278
# Dislikes: 378
# Total Accepted:    22.8K
# Total Submissions: 89.8K
# Testcase Example:  '"*"'
#
# 
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping way:
# 
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 
# Beyond that, now the encoded string can also contain the character '*', which
# can be treated as one of the numbers from 1 to 9.
# 
# 
# 
# 
# Given the encoded message containing digits and the character '*', return the
# total number of ways to decode it.
# 
# 
# 
# Also, since the answer may be very large, you should return the output mod
# 10^9 + 7.
# 
# 
# Example 1:
# 
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C",
# "D", "E", "F", "G", "H", "I".
# 
# 
# 
# Example 2:
# 
# Input: "1*"
# Output: 9 + 9 = 18
# 
# 
# 
# Note:
# 
# The length of the input string will fit in range [1, 10^5].
# The input string will only contain the character '*' and digits '0' - '9'.
# 
# 
#
class Solution:
    def numDecodings(self, s: str) -> int:
        # O(n)
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1, '21': 1,
            '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2, '*6': 2,
            '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}

        dp0, dp1 = 1, one.get(s[:1], 0)
        for i in range(1, len(s)):
            dp0, dp1 = dp1, (one.get(s[i], 0)  * dp1 + two.get(s[i-1:i+1], 0) * dp0) % (10**9 + 7)

        return dp1

        

