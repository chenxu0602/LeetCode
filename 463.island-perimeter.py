#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (62.68%)
# Likes:    1425
# Dislikes: 97
# Total Accepted:    164.6K
# Total Submissions: 262.6K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands, neighbors = 0, 0
        m, n = len(grid), len(grid[0]) if grid else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    if i < m - 1 and grid[i+1][j] == 1:
                        neighbors += 1
                    if j < n - 1 and grid[i][j+1] == 1:
                        neighbors += 1

        return islands * 4 - neighbors * 2
        
# @lc code=end

