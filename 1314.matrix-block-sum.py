#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#
# https://leetcode.com/problems/matrix-block-sum/description/
#
# algorithms
# Medium (71.79%)
# Likes:    101
# Dislikes: 17
# Total Accepted:    5.5K
# Total Submissions: 7.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a m * n matrix mat and an integer K, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j
# - K <= c <= j + K, and (r, c) is a valid position in the matrix.
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
# 
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = map(len, (mat, mat[0]))
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sums[i][j] = mat[i - 1][j - 1] + sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1]

        answers = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row1 = max(0, i - K)
                col1 = max(0, j - K)
                row2 = min(m - 1, i + K)
                col2 = min(n - 1, j + K)
                answers[i][j] = sums[row2 + 1][col2 + 1] - sums[row2 + 1][col1] - sums[row1][col2 + 1] + sums[row1][col1]

        return answers

# @lc code=end

