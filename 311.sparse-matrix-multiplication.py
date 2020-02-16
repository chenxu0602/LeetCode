#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#
# https://leetcode.com/problems/sparse-matrix-multiplication/description/
#
# algorithms
# Medium (58.94%)
# Likes:    357
# Dislikes: 142
# Total Accepted:    78.3K
# Total Submissions: 132.8K
# Testcase Example:  '[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]'
#
# Given two sparse matrices A and B, return the result of AB.
# 
# You may assume that A's column number is equal to B's row number.
# 
# Example:
# 
# 
# Input:
# 
# A = [
# ⁠ [ 1, 0, 0],
# ⁠ [-1, 0, 3]
# ]
# 
# B = [
# ⁠ [ 7, 0, 0 ],
# ⁠ [ 0, 0, 0 ],
# ⁠ [ 0, 0, 1 ]
# ]
# 
# Output:
# 
# ⁠    |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
# ⁠                 | 0 0 1 |
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        def compress(mat):
            return [
                [i, j, num]
                for i, row in enumerate(mat)
                for j, num in enumerate(row) if num
            ]

        m, n = len(A), len(B[0])
        r = [[0] * n for _ in range(m)]

        A, B = map(compress, (A, B))
        [r[rowA].__setitem__(colB, r[rowA][colB] + numA * numB)
            for rowA, colA, numA in A
            for rowB, colB, numB in B if colA == rowB
        ]

        return r
        
# @lc code=end

