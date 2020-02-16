#
# @lc app=leetcode id=1284 lang=python3
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
#
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description/
#
# algorithms
# Hard (69.58%)
# Likes:    98
# Dislikes: 14
# Total Accepted:    4.7K
# Total Submissions: 6.8K
# Testcase Example:  '[[0,0],[0,1]]\r'
#
# Given a m x n binary matrix mat. In one step, you can choose one cell and
# flip it and all the four neighbours of it if they exist (Flip is changing 1
# to 0 and 0 to 1). A pair of cells are called neighboors if they share one
# edge.
# 
# Return the minimum number of steps required to convert mat to a zero matrix
# or -1 if you cannot.
# 
# Binary matrix is a matrix with all cells equal to 0 or 1 only.
# 
# Zero matrix is a matrix with all cells equal to 0.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally
# (1, 1) as shown.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We don't need to change it.
# 
# 
# Example 3:
# 
# 
# Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
# Output: 6
# 
# 
# Example 4:
# 
# 
# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix can't be a zero matrix
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[0].length
# 1 <= m <= 3
# 1 <= n <= 3
# mat[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        board = mat
        M, N = len(board), len(board[0])
        coeff = [[0] * (M * N) for _ in range(M * N)]
        y = [0] * (M * N)

        def zadd(coeff, y, i, j):
            for k in range(M * N):
                coeff[j][k] = (coeff[j][k] + coeff[i][k]) & 1
            y[j] = (y[i] + y[j]) & 1

        if not board or not board[0]: return -1

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                index = i * N + j
                if val == 1: y[index] = 1
                for ni, nj in (i-1, j), (i, j-1), (i, j), (i+1, j), (i, j+1):
                    if 0 <= ni < M and 0 <= nj < N:
                        coeff[index][ni * N + nj] = 1

        for i in range(i, M * N - 1):
            for j in range(i, M * N):
                if coeff[j][i] == 1:
                    coeff[j], coeff[i] = coeff[i], coeff[j] 
                    y[j], y[i] = y[i], y[j]
                    break
            else:
                continue
            for j in range(i+1, M * N):
                if coeff[j][i] == 1:
                    zadd(coeff, y, i, j)


        for i in range(M * N - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if coeff[j][i] == 1:
                    zadd(coeff, y, i, j)

        clicks = []
        res = 0
        for i in range(M * N):
            if y[i] == 1:
                if coeff[i][i] == 1:
                    res += 1
                    clicks.append((i // N, i % N))
                else:
                    return -1

        return res
        
        
# @lc code=end

