#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (45.48%)
# Likes:    377
# Dislikes: 230
# Total Accepted:    45.6K
# Total Submissions: 100.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        if not matrix: return []
        res = []
        lines = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lines[i+j].append(matrix[i][j])

        for k in range(len(matrix) + len(matrix[0]) - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res
        """

        # m, n, r = len(matrix), len(matrix) and len(matrix[0]), []
        # for l in range(m + n - 1):
        #     temp = [matrix[i][l - i] for i in range(max(0, l+1 - n), min(l+1, m))]
        #     r += temp if l % 2 else temp[::-1]
        # return r

        if not matrix: return []
        res = []
        lines = defaultdict(list)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lines[i+j].append(matrix[i][j])

        for k in range(len(matrix) + len(matrix[0]) - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res

        

        

