#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (36.17%)
# Likes:    729
# Dislikes: 79
# Total Accepted:    48K
# Total Submissions: 132.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# 
# Example 1: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
# 
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
# 
# 
# Example 2: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
# 
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
# 
# 
# 
# 
# Note:
# 
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
#
from math import inf 

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    top = matrix[i-1][j] if i > 0 else inf
                    left = matrix[i][j-1] if j > 0 else inf
                    matrix[i][j] = min(top, left) + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] != 0:
                    bottom = matrix[i+1][j] if i < m - 1 else inf
                    right = matrix[i][j+1] if j < n - 1 else inf

                    matrix[i][j] = min(matrix[i][j], min(bottom, right) + 1)

        return matrix
        

