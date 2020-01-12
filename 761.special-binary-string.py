#
# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#
# https://leetcode.com/problems/special-binary-string/description/
#
# algorithms
# Hard (52.62%)
# Likes:    191
# Dislikes: 74
# Total Accepted:    5.4K
# Total Submissions: 10.3K
# Testcase Example:  '"11011000"'
#
# 
# Special binary strings are binary strings with the following two properties:
# 
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# 
# Given a special string S, a move consists of choosing two consecutive,
# non-empty, special substrings of S, and swapping them.  (Two strings are
# consecutive if the last character of the first string is exactly one index
# before the first character of the second string.)
# 
# At the end of any number of moves, what is the lexicographically largest
# resulting string possible?
# 
# 
# Example 1:
# 
# Input: S = "11011000"
# Output: "11100100"
# Explanation:
# The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
# This is the lexicographically largest string possible after some number of
# swaps.
# 
# 
# 
# Note:
# S has length at most 50.
# S is guaranteed to be a special binary string as defined above.
# 
#
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        if not S: return S
        mountains = []
        anchor = bal = 0
        for i, v in enumerate(S):
            bal += 1 if v == '1' else -1
            if bal == 0:
                mountains.append("1{}0".format(
                    self.makeLargestSpecial(S[anchor+1: i])))
                anchor = i + 1

        mountains.sort(reverse=True)
        return "".join(mountains)
            
        

