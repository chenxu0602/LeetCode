#
# @lc app=leetcode id=2684 lang=python3
#
# [2684] Maximum Number of Moves in a Grid
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = map(len, (grid, grid[0]))
        
        @lru_cache(None)
        def dp(i, j):
            ans = 0
            for di, dj in (-1, 1), (1, 1), (0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] < grid[ni][nj]:
                    ans = max(ans, 1 + dp(ni, nj))

            return ans

        return max(dp(i, 0) for i in range(m))
        
# @lc code=end

