#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
#
# algorithms
# Medium (58.09%)
# Likes:    273
# Dislikes: 7
# Total Accepted:    6.1K
# Total Submissions: 10.4K
# Testcase Example:  '[[0,0,1],[1,1,1],[1,0,1]]'
#
# You are given a binary matrix matrix of size m x n, and you are allowed to
# rearrange the columns of the matrix in any order.
# 
# Return the area of the largest submatrix within matrix where every element of
# the submatrix is 1 after reordering the columns optimally.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no
# way to make a submatrix of 1s larger than an area of 2.
# 
# Example 4:
# 
# 
# Input: matrix = [[0,0],[0,0]]
# Output: 0
# Explanation: As there are no 1s, no submatrix of 1s can be formed and the
# area is 0.
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10^5
# matrix[i][j] is 0 or 1.
# 
#

# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Time  complexity: O(n x mlogm)
        # Space complexity: O(m)
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr = sorted(matrix[row], reverse=True)
            for i in range(len(matrix[0])):
                ans = max(ans, curr[i] * (i + 1))

        return ans
        
# @lc code=end

