#
# @lc app=leetcode id=2658 lang=python3
#
# [2658] Maximum Number of Fish in a Grid
#

# @lc code=start
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        m, n = map(len, (grid, grid[0]))
        self.ans = 0

        def dfs(r, c, grid):
            val = grid[r][c]
            grid[r][c] = 0
            res = val
            for dr, dc in (1, 0), (-1, 0), (0, -1), (0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    res += dfs(nr, nc, grid)

            return res

            


        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    self.ans = max(self.ans, dfs(i, j, grid))

        return self.ans
        
# @lc code=end

