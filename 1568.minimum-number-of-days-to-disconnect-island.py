#
# @lc app=leetcode id=1568 lang=python3
#
# [1568] Minimum Number of Days to Disconnect Island
#
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
#
# algorithms
# Hard (50.75%)
# Likes:    158
# Dislikes: 94
# Total Accepted:    5.2K
# Total Submissions: 10.2K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,0]]'
#
# Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a
# maximal 4-directionally (horizontal or vertical) connected group of 1s.
# 
# The grid is said to be connected if we have exactly one island, otherwise is
# said disconnected.
# 
# In one day, we are allowed to change any single land cell (1) into a water
# cell (0).
# 
# Return the minimum number of days to disconnect the grid.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected
# island.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0
# islands.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,1,0]]
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: grid = [[1,1,0,1,1],
# [1,1,1,1,1],
# [1,1,0,1,1],
# [1,1,0,1,1]]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: grid = [[1,1,0,1,1],
# [1,1,1,1,1],
# [1,1,0,1,1],
# [1,1,1,1,1]]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
import copy

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # def no_islands_recur(grid, i, j, m, n):
        #     if grid[i][j] == 0:
        #         return
        #     grid[i][j] = 0
        #     if i - 1 >= 0:
        #         no_islands_recur(grid, i - 1, j, m, n)
        #     if i + 1 < m:
        #         no_islands_recur(grid, i + 1, j, m, n)
        #     if j - 1 >= 0:
        #         no_islands_recur(grid, i, j - 1, m, n)
        #     if j + 1 < n:
        #         no_islands_recur(grid, i, j + 1, m, n)

        # #find how many islands the given grid has      
        # def no_islands(grid):
        #     ret = 0
        #     m, n = map(len, (grid, grid[0]))
        #     for i in range(m):
        #         for j in range(n):
        #             if grid[i][j] == 1:
        #                 ret += 1
        #                 no_islands_recur(grid, i, j, m, n)
        #     return ret


        # time = 0
        # grid_copy = copy.deepcopy(grid)
        # n = no_islands(grid_copy)
        # if n != 1: return time

        # time = 1
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         grid_copy = copy.deepcopy(grid)
        #         grid_copy[i][j] = 0
        #         n = no_islands(grid_copy)
        #         if n != 1:
        #             return time 

        # time = 2
        # return time


        def dfs(grid, r, c, visited):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                dfs(grid, r + 1, c, visited)
                dfs(grid, r - 1, c, visited)
                dfs(grid, r, c + 1, visited)
                dfs(grid, r, c - 1, visited)

        def countIslands(grid):
            islands = 0
            visited = set()

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        islands += 1
                        dfs(grid, r, c, visited)

            return islands

        
        if countIslands(grid) != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    if countIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1

        return 2

        
# @lc code=end

