#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
#
# algorithms
# Medium (79.07%)
# Likes:    471
# Dislikes: 115
# Total Accepted:    23.4K
# Total Submissions: 29.6K
# Testcase Example:  '[[3,3,1,1],[2,2,1,2],[1,1,1,2]]'
#
# Given a m * n matrix mat of integers, sort it diagonally in ascending order
# from the top-left to the bottom-right then return the sorted array.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = map(len, (mat, mat[0]))
        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[j - i].append(mat[i][j])

        for k in d:
            d[k].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = d[j - i].pop()

        return mat
        
# @lc code=end

