#
# @lc app=leetcode id=816 lang=python3
#
# [816] Ambiguous Coordinates
#
# https://leetcode.com/problems/ambiguous-coordinates/description/
#
# algorithms
# Medium (44.81%)
# Likes:    85
# Dislikes: 176
# Total Accepted:    7.4K
# Total Submissions: 16.5K
# Testcase Example:  '"(123)"'
#
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we
# removed all commas, decimal points, and spaces, and ended up with the string
# S.  Return a list of strings representing all possibilities for what our
# original coordinates could have been.
# 
# Our original representation never had extraneous zeroes, so we never started
# with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
# number that can be represented with less digits.  Also, a decimal point
# within a number never occurs without at least one digit occuring before it,
# so we never started with numbers like ".1".
# 
# The final answer list can be returned in any order.  Also note that all
# coordinates in the final answer have exactly one space between them
# (occurring after the comma.)
# 
# 
# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# 
# 
# 
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation: 
# 0.0, 00, 0001 or 00.01 are not allowed.
# 
# 
# 
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)",
# "(0.12, 3)"]
# 
# 
# 
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation: 
# 1.0 is not allowed.
# 
# 
# 
# 
# Note: 
# 
# 
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are
# digits.
# 
# 
# 
# 
#
import itertools

class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        # O(N^3)
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                     and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right


        S = S[1:-1]
        return ["({}, {})".format(*cand) for i in range(1, len(S)) for cand in itertools.product(make(S[:i]), make(S[i:]))]
        

