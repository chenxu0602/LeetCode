#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#
# https://leetcode.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (70.49%)
# Likes:    303
# Dislikes: 82
# Total Accepted:    14.8K
# Total Submissions: 21K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# We have a two dimensional matrix A where each value is 0 or 1.
# 
# A move consists of choosing any row or column, and toggling each value in
# that row or column: changing all 0s to 1s, and all 1s to 0s.
# 
# After making any number of moves, every row of this matrix is interpreted as
# a binary number, and the score of the matrix is the sum of these numbers.
# 
# Return the highest possible score.
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
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.
# 
# 
# 
#
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:

        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans
        

