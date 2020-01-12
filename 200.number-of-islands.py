#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.09%)
# Likes:    2843
# Dislikes: 100
# Total Accepted:    386.6K
# Total Submissions: 915.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
        """

        def dfs(grid, r, c, m, n):
            grid[r][c] = '0'
            if 0 <= r - 1 and grid[r-1][c] == '1':
                dfs(grid, r - 1, c, m, n)
            if r + 1 < m and grid[r+1][c] == '1':
                dfs(grid, r + 1, c, m, n)
            if 0 <= c - 1 and grid[r][c-1] == '1':
                dfs(grid, r, c - 1, m, n)
            if c + 1 < n and grid[r][c+1] == '1':
                dfs(grid, r, c + 1, m, n)

        if not grid: return 0

        num_islands = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(grid, r, c, m, n)

        return num_islands
        """

        
        

