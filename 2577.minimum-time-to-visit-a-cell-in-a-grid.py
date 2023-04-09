#
# @lc app=leetcode id=2577 lang=python3
#
# [2577] Minimum Time to Visit a Cell In a Grid
#

# @lc code=start
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        # We can wait by playing "ping pong" between previous cell and current cell till a neighboring cell opens up.

        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n = map(len, (grid, grid[0]))
        visited = set()
        pq = [(grid[0][0], 0, 0)]

        while pq:
            time, r, c = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return time

            if (r, c) in visited: continue

            visited.add((r, c))

            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    wait = 1 if (grid[nr][nc] - time) % 2 == 0 else 0
                    heapq.heappush(pq, (max(time + 1, grid[nr][nc] + wait), nr, nc))
        
# @lc code=end

