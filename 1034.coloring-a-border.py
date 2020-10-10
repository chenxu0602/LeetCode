#
# @lc app=leetcode id=1034 lang=python3
#
# [1034] Coloring A Border
#
# https://leetcode.com/problems/coloring-a-border/description/
#
# algorithms
# Medium (44.65%)
# Likes:    142
# Dislikes: 280
# Total Accepted:    11.3K
# Total Submissions: 25.2K
# Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
#
# Given a 2-dimensional grid of integers, each value in the grid represents the
# color of the grid square at that location.
# 
# Two squares belong to the same connected component if and only if they have
# the same color and are next to each other in any of the 4 directions.
# 
# The border of a connected component is all the squares in the connected
# component that are either 4-directionally adjacent to a square not in the
# component, or on the boundary of the grid (the first or last row or column).
# 
# Given a square at location (r0, c0) in the grid and a color, color the border
# of the connected component of that square with the given color, and return
# the final grid.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# Output: [[3, 3], [3, 2]]
# 
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# Output: [[1, 3, 3], [2, 3, 3]]
# 
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 50
# 1 <= grid[0].length <= 50
# 1 <= grid[i][j] <= 1000
# 0 <= r0 < grid.length
# 0 <= c0 < grid[0].length
# 1 <= color <= 1000
# 
#

# @lc code=start
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        # seen, m, n = set(), len(grid), len(grid[0])

        # def dfs(x, y):
        #     if (x, y) in seen:
        #         return True

        #     if not (0 <= x < m and 0 <= y < n and grid[x][y] == grid[r0][c0]):
        #         return False

        #     seen.add((x, y))

        #     if dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) < 4:
        #         grid[x][y] = color

        #     return True

        # dfs(r0, c0)
        # return grid


        m, n = map(len, (grid, grid[0]))
        bfs, component, border = [[r0, c0]], set([(r0, c0)]), set()

        for r0, c0 in bfs:
            for i, j in (0, 1), (1, 0), (-1, 0), (0, -1):
                r, c = r0 + i, c0 + j
                if 0 <= r < m and 0 <= c < n and grid[r][c] == grid[r0][c0]:
                    if (r, c) not in component:
                        bfs.append((r, c))
                        component.add((r, c))
                else:
                    border.add((r0, c0))

        for x, y in border:
            grid[x][y] = color

        return grid
        
# @lc code=end

