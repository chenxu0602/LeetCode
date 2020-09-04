#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (39.09%)
# Likes:    426
# Dislikes: 231
# Total Accepted:    15.6K
# Total Submissions: 39.7K
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

# @lc code=start
class Solution:
    def numTilings(self, N: int) -> int:
        # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116612/Easy-to-understand-O(n)-solution-with-Drawing-Picture-Explanation!
        # O(N)
        # MOD = 10**9 + 7
        # g, u = [0] * (1000 + 1), [0] * (1000 + 1)
        # g[0], g[1], g[2] = 0, 1, 2
        # u[0], u[1], u[2] = 0, 1, 2

        # for i in range(3, N + 1):
        #     u[i] = (u[i - 1] + g[i - 1]) % MOD
        #     g[i] = (g[i - 1] + g[i - 2] + 2 * u[i - 2]) % MOD

        # return g[N] % MOD


        # O(logN)
        MOD = 10**9 + 7

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a * b for a, b in zip(row, col)) % MOD
                     for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i == j) for j in range(len(A))] for i in range(len(A))]

            if K == 1: 
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K - 1), A)

            B = matrix_expo(A, K // 2)
            return matrix_mult(B, B)

        T = [[1, 0, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 0]]

        return matrix_expo(T, N)[0][0]

        
# @lc code=end

