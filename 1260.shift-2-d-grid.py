#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#
# https://leetcode.com/problems/shift-2d-grid/description/
#
# algorithms
# Easy (60.43%)
# Likes:    107
# Dislikes: 62
# Total Accepted:    10.5K
# Total Submissions: 17.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a 2D grid of size m x n and an integer k. You need to shift the grid k
# times.
# 
# In one shift operation:
# 
# 
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# 
# 
# Return the 2D grid after applying shift operation k times.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# 
# 
# Example 2:
# 
# 
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100
# 
# 
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        # num_rows, num_cols = len(grid), len(grid[0])

        # for _ in range(k):
        #     previous = grid[-1][-1]
        #     for row in range(num_rows):
        #         for col in range(num_cols):
        #             temp = grid[row][col]
        #             grid[row][col] = previous
        #             previous = temp

        # return grid

        num_rows, num_cols = len(grid), len(grid[0])
        new_grid = [[0] * num_cols for _ in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col + k) % num_cols
                wrap_around_count = (col + k) // num_cols
                new_row = (row + wrap_around_count) % num_rows
                new_grid[new_row][new_col] = grid[row][col]

        return new_grid


        
# @lc code=end

