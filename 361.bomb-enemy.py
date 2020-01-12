#
# @lc app=leetcode id=361 lang=python3
#
# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (43.37%)
# Likes:    286
# Dislikes: 57
# Total Accepted:    34.6K
# Total Submissions: 79.7K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.
# 
# Example:
# 
# 
# 
# Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3 
# Explanation: For the given grid,
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# Placing a bomb at (1,1) kills 3 enemies.
# 
# 
#
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        def hits(grid):
            return [[h for block in ''.join(row).split('W')
                       for h in [block.count('E')] * len(block) + [0]]
                       for row in grid]

        
        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        return max([rh + ch 
                    for row in zip(grid, rowhits, colhits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])
        """

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        bombs = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 'E']
        for x, y in bombs:
            nx, ny = x, y
            while True:
                if 0 <= nx+1 < m:
                    if grid[nx+1][ny] == 'W':
                        break
                    if grid[nx+1][ny].isdigit():
                        grid[nx+1][ny] = str(int(grid[nx+1][ny]) + 1)
                        nx += 1
                    else:
                        nx += 1
                else:
                    break


            nx, ny = x, y
            while True:
                if 0 <= nx-1 < m:
                    if grid[nx-1][ny] == 'W':
                        break
                    if grid[nx-1][ny].isdigit():
                        grid[nx-1][ny] = str(int(grid[nx-1][ny]) + 1)
                        nx -= 1
                    else:
                        nx -= 1
                else:
                    break

            nx, ny = x, y
            while True:
                if 0 <= ny+1 < n:
                    if grid[nx][ny+1] == 'W':
                        break
                    if grid[nx][ny+1].isdigit():
                        grid[nx][ny+1] = str(int(grid[nx][ny+1]) + 1)
                        ny += 1
                    else:
                        ny += 1
                else:
                    break

            nx, ny = x, y
            while True:
                if 0 <= ny-1 < n:
                    if grid[nx][ny-1] == 'W':
                        break
                    if grid[nx][ny-1].isdigit():
                        grid[nx][ny-1] = str(int(grid[nx][ny-1]) + 1)
                        ny -= 1
                    else:
                        ny -= 1
                else:
                    break

        res = [int(grid[i][j]) for i in range(m) for j in range(n) if grid[i][j].isdigit()] 
        if res:
            return max(res)
        else:
            return 0

