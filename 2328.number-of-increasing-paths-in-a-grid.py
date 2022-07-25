#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start
from functools import lru_cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # O(mn)

        m, n = map(len, (grid, grid[0]))
        MOD = 10**9 + 7

        @lru_cache(None)
        def count(i, j):
            res = 1
            for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                    res += count(x, y) % MOD
            return res

        return sum(count(i, j) for i in range(m) for j in range(n)) % MOD
        
# @lc code=end

