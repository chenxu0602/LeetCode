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
        def compress(matrix):
            return [
                [i, j, num]
                for i, row in enumerate(matrix)
                for j, num in enumerate(row) if num
            ]

        cpA, cpB = map(compress, (A, B))
        r = [[0] * len(B[0]) for _ in range(len(A))]

        # for rowA, colA, numA in cpA:
        #     for rowB, colB, numB in cpB:
        #         if colA == rowB:
        #             r[rowA][colB] += numA * numB


        [r[rowA].__setitem__(colB, r[rowA][colB] + numA * numB)
         for rowA, colA, numA in cpA
         for rowB, colB, numB in cpB if colA == rowB]

        return r
        
# @lc code=end

