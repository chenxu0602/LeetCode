#
# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (59.30%)
# Likes:    58
# Dislikes: 212
# Total Accepted:    9.3K
# Total Submissions: 15.8K
# Testcase Example:  '"0110"\n3'
#
# Given a binary string S (a string consisting only of '0' and '1's) and a
# positive integer N, return true if and only if for every integer X from 1 to
# N, the binary representation of X is a substring of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "0110", N = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: S = "0110", N = 4
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 1000
# 1 <= N <= 10^9
# 
# 
#
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        # suppose that N > 2047 then S must contains substrings of length 11 that represents all 1024 numbers from 1024 to 2047. But it is not possible because S is 1000 long so it can have at most 989 substrings of length 11. So we just need to check if N <= 2047.
        return all(bin(i)[2:] in S for i in range(N, N//2, -1))
        

