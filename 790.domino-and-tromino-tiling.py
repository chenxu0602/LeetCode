#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (36.54%)
# Likes:    269
# Dislikes: 139
# Total Accepted:    9.4K
# Total Submissions: 25.6K
# Testcase Example:  '3'
#
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
# 
# 
# XX  <- domino
# 
# XX  <- "L" tromino
# X
# 
# 
# Given N, how many ways are there to tile a 2 x N board? Return your answer
# modulo 10^9 + 7.
# 
# (In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.)
# 
# 
# 
# Example:
# Input: 3
# Output: 5
# Explanation: 
# The five different ways are listed below, different letters indicates
# different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# 
# Note:
# 
# 
# N  will be in range [1, 1000].
# 
# 
# 
# 
#
import numpy as np

class Solution:
    def numTilings(self, N: int) -> int:
        """
        if N <= 1:
            return 1
        elif N == 2:
            return 2

        x = np.array([2, 1, 1], dtype=np.int64)
        A = np.array([[2, 1, 1], [3, 1, 1], [4, 2, 1]], dtype=np.int64)
        y1 = np.array([1, 1, 2], dtype=np.int64)
        y2 = np.array([2, 3, 4], dtype=np.int64)

        if N % 2 == 1:
            k = (N - 3) // 2
            y = y1
        else:
            k = (N - 4) // 2
            y = y2

        xA = x
        while k > 0:
            if k % 2 == 1:
                xA = xA.dot(A) % 1000000007

            k //= 2
            A = A.dot(A) % 1000000007
        return int(xA.dot(y) % 1000000007)
        """

        A = [0] * (N + 1)
        B = [1, 1] + [0] * (N - 1)
        for i in range(2, N + 1):
            A[i] = (B[i - 2] + A[i - 1]) % int(1e9 + 7)
            B[i] = (B[i - 1] + B[i - 2] + A[i - 1] * 2) % int(1e9 + 7)
        return B[N]

        
        

