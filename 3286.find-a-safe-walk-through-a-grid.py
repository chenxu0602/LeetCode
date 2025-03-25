#
# @lc app=leetcode id=3286 lang=python3
#
# [3286] Find a Safe Walk Through a Grid
#

# @lc code=start
from heapq import heappush, heappop
from functools import lru_cache
from itertools import product

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        # Dijkstra
        # Time  complexity: O(mn x log(mn))
        # Space complexity: O(mn)
        m, n = map(len, (grid, grid[0]))
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = -health + grid[0][0]
        pq = [(dist[0][0], 0, 0)]

        while pq:
            d, i, j = heappop(pq)
            for di, dj in (1, 0), (-1, 0), (0, -1), (0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if d + grid[ni][nj] < dist[ni][nj]:
                        dist[ni][nj] = d + grid[ni][nj]
                        heappush(pq, (d + grid[ni][nj], ni, nj))

        return dist[m - 1][n - 1] < 0


        """
        # DFS
        # Time  complexity: O(mn x health)
        # Space complexity: O(mn x health)
        @lru_cache(None)
        def dp(x, y, health_used):
            nonlocal eligible
            if health_used == health or (x, y) not in eligible:
                return float('inf')

            health_to_use = health_used + grid[x][y]
            if (x, y) == (m - 1, n - 1): return health_to_use

            eligible.discard((x, y))

            res = min(
                dp(x + 1, y, health_to_use), 
                dp(x, y + 1, health_to_use),
                dp(x - 1, y, health_to_use),
                dp(x, y - 1, health_to_use))

            eligible.add((x, y))

            return res


        m, n = map(len, (grid, grid[0]))
        eligible = set(product(range(m), range(n)))

        return dp(0, 0, 0) < health
        """

        
# @lc code=end

