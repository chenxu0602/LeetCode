#
# @lc app=leetcode id=3283 lang=python3
#
# [3283] Maximum Number of Moves to Kill All Pawns
#

# @lc code=start
from functools import lru_cache
from collections import deque

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:

        n = len(positions)
        dist = [[0] * n for _ in range(n + 1)]
        positions += [kx, ky],

        def bfs(i):
            queue = deque([positions[i]])
            seen, step = set(), 0
            while queue:
                l = len(queue)
                for _ in range(l):
                    x, y = queue.popleft()
                    if [x, y] == positions[j]: return step
                    for dx, dy in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 50 and 0 <= ny < 50 and not (nx, ny) in seen:
                            queue.append([nx, ny])
                            seen.add((nx, ny))

                step += 1

        for i in range(n + 1):
            for j in range(n):
                if i != j:
                    dist[i][j] = bfs(i)

        ops = [max, min]
        init = [0, float('inf')]

        @lru_cache(None)
        def dp(i, mask, player):
            if mask == (1 << n) - 1: return 0
            ans = init[player]
            for j in range(n):
                if mask & (1 << j): continue
                ans = ops[player](ans, dist[i][j] + dp(j, mask | (1 << j), player ^ 1))
            return ans
        
        return dp(n, 0, 0)

        
# @lc code=end

