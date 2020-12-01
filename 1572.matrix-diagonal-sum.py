#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#
# https://leetcode.com/problems/matrix-diagonal-sum/description/
#
# algorithms
# Easy (78.32%)
# Likes:    242
# Dislikes: 6
# Total Accepted:    27K
# Total Submissions: 34.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square matrix mat, return the sum of the matrix diagonals.
# 
# Only include the sum of all the elements on the primary diagonal and all the
# elements on the secondary diagonal that are not part of the primary
# diagonal.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],
# [4,5,6],
# [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,1,1,1],
# [1,1,1,1],
# [1,1,1,1],
# [1,1,1,1]]
# Output: 8
# 
# 
# Example 3:
# 
# 
# Input: mat = [[5]]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 0: return 0

        res = sum(mat[i][i] for i in range(n))
        res += sum(mat[i][n - i - 1] for i in range(n))

        if n % 2:
            res -= mat[n//2][n//2]

        return res
        
# @lc code=end

