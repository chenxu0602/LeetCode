#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
# https://leetcode.com/problems/binary-gap/description/
#
# algorithms
# Easy (59.73%)
# Likes:    143
# Dislikes: 369
# Total Accepted:    27.7K
# Total Submissions: 46.3K
# Testcase Example:  '22'
#
# Given a positive integer N, find and return the longest distance between two
# consecutive 1's in the binary representation of N.
# 
# If there aren't two consecutive 1's, return 0.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 22
# Output: 2
# Explanation: 
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive
# pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: 2
# Explanation: 
# 5 in binary is 0b101.
# 
# 
# 
# Example 3:
# 
# 
# Input: 6
# Output: 1
# Explanation: 
# 6 in binary is 0b110.
# 
# 
# 
# Example 4:
# 
# 
# Input: 8
# Output: 0
# Explanation: 
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8,
# so we return 0.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def binaryGap(self, N: int) -> int:

        """
        idxs = [i for i, x in enumerate(list(bin(N))) if x == '1']
        if len(idxs) > 1:
            diffs = [abs(j-i) for i, j in zip(idxs, idxs[1:])]
            return max(diffs)
        else:
            return 0
        """

        A = [i for i in range(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in range(len(A)-1))
        

