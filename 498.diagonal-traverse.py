#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (46.63%)
# Likes:    537
# Dislikes: 276
# Total Accepted:    63.2K
# Total Submissions: 135.5K
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

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, r = len(matrix), len(matrix) and len(matrix[0]), []
        for l in range(m + n - 1):
            temp = [matrix[i][l-i] for i in range(max(0, l + 1 - n), min(l + 1, m))]
            r += temp if l % 2 else temp[::-1]
        return r
        
# @lc code=end

