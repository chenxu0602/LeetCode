#
# @lc app=leetcode id=1111 lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
#
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/
#
# algorithms
# Medium (65.42%)
# Likes:    59
# Dislikes: 258
# Total Accepted:    4.6K
# Total Submissions: 6.9K
# Testcase Example:  '"(()())"'
#
# A string is a valid parentheses string (denoted VPS) if and only if it
# consists of "(" and ")" characters only, and:
# 
# 
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are VPS's,
# or
# It can be written as (A), where A is a VPS.
# 
# 
# We can similarly define the nesting depth depth(S) of any VPS S as
# follows:
# 
# 
# depth("") = 0
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# 
# 
# For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1,
# and 2), and ")(" and "(()" are not VPS's.
# 
# 
# 
# Given a VPS seq, split it into two disjoint subsequences A and B, such that A
# and B are VPS's (and A.length + B.length = seq.length).
# 
# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum
# possible value.
# 
# Return an answer array (of length seq.length) that encodes such a choice of A
# and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that
# even though multiple answers may exist, you may return any of them.
# 
# 
# Example 1:
# 
# 
# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]
# 
# 
# Example 2:
# 
# 
# Input: seq = "()(())()"
# Output: [0,0,0,1,1,0,1,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= seq.size <= 10000
# 
# 
#
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        A = B = 0
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            v = 1 if c == '(' else -1
            if (v > 0) == (A < B):
                A += v
            else:
                B += v
                res[i] = 1
        return res
        """

        return [i & 1 ^ (seq[i] == '(') for i, c in enumerate(seq)]
        

