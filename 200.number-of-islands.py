#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.58%)
# Likes:    4056
# Dislikes: 150
# Total Accepted:    539.1K
# Total Submissions: 1.2M
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

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS O(M x N)
        # def dfs(grid, r, c):
        #     if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
        #         return

        #     grid[r][c] = '0'
        #     dfs(grid, r - 1, c)
        #     dfs(grid, r + 1, c)
        #     dfs(grid, r, c - 1)
        #     dfs(grid, r, c + 1)

        # if not grid: return 0
        # m, n = map(len, (grid, grid[0]))
        # num_islands = 0
        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] == '1':
        #             num_islands += 1
        #             dfs(grid, r, c)

        # return num_islands

        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
        
# @lc code=end

