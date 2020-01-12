#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (35.23%)
# Likes:    296
# Dislikes: 102
# Total Accepted:    12.7K
# Total Submissions: 36.1K
# Testcase Example:  '"123456579"'
#
# Given a string S of digits, such as S = "123456579", we can split it into a
# Fibonacci-like sequence [123, 456, 579].
# 
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such
# that:
# 
# 
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
# type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# 
# 
# Also, note that when splitting the string into pieces, each piece must not
# have extra leading zeroes, except if the piece is the number 0 itself.
# 
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be
# done.
# 
# Example 1:
# 
# 
# Input: "123456579"
# Output: [123,456,579]
# 
# 
# Example 2:
# 
# 
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# 
# 
# Example 3:
# 
# 
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# 
# 
# Example 4:
# 
# 
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
# 
# 
# Example 5:
# 
# 
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# 
# 
# Note: 
# 
# 
# 1 <= S.length <= 200
# S contains only digits.
# 
# 
#
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        L, T, t = len(S), "", []
        for i in range(1, L-2):
            for j in range(1, L-i-1):
                if (i > 1 and S[0] == '0') or (j > 1 and S[i] == '0'):
                    continue
                a, b = int(S[:i]), int(S[i:i+j])
                T, t = S[:i+j], [a, b]
                while len(T) < L:
                    c = a + b
                    T += str(c)
                    t += [c]
                    a, b = b, c
                if len(T) == L and T == S and len(t) > 2 and t[-1] < 2**31 - 1:
                    return t
        return []
        

