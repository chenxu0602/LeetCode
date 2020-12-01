#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
#
# algorithms
# Easy (64.31%)
# Likes:    163
# Dislikes: 6
# Total Accepted:    16K
# Total Submissions: 24.9K
# Testcase Example:  '[[1,0,0],[0,0,1],[1,0,0]]'
#
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the
# number of special positions in mat.
# 
# A position (i,j) is called special if mat[i][j] == 1 and all other elements
# in row i and column j are 0 (rows and columns are 0-indexed).
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,0,0],
# [0,0,1],
# [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other
# elements in row 1 and column 2 are 0.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,0,0],
# [0,1,0],
# [0,0,1]]
# Output: 3
# Explanation: (0,0), (1,1) and (2,2) are special positions. 
# 
# 
# Example 3:
# 
# 
# Input: mat = [[0,0,0,1],
# [1,0,0,0],
# [0,1,1,0],
# [0,0,0,0]]
# Output: 2
# 
# 
# Example 4:
# 
# 
# Input: mat = [[0,0,0,0,0],
# [1,0,0,0,0],
# [0,1,0,0,0],
# [0,0,1,0,0],
# [0,0,0,1,1]]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = map(len, (mat, mat[0]))
        matT = list(zip(*mat))
        ans = 0

        for r, row in enumerate(mat):
            if row.count(1) == 1:
                c = row.index(1)
                if (r == 0 or set(matT[c][:r]) == {0}) and (r + 1 == m or set(matT[c][r + 1:]) == {0}):
                    ans += 1

        return ans
        
# @lc code=end

