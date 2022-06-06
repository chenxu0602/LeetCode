#
# @lc app=leetcode id=2258 lang=python3
#
# [2258] Escape the Spreading Fire
#

# @lc code=start
from collections import deque
import bisect

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        fire_moves = [[-1] * n for _ in range(m)]
        person_moves = [[-1] * n for _ in range(m)]

        def bfs(frontier, board, is_fire=True):
            while frontier:
                r, c, step = frontier.popleft()
                board[r][c] = step
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] < 0 and \
                        grid[nr][nc] != 2 and (is_fire or fire_moves[nr][nc] < 0 or fire_moves[nr][nc] > step + 1 or (
                            fire_moves[nr][nc] == step + 1 and nr == m - 1 and nc == n - 1)):
                        frontier.append((nr, nc, step + 1))

        bfs(deque([(r, c, 0) for r in range(m) for c in range(n) if grid[r][c] == 1]), fire_moves)
        bfs(deque([(0, 0, 0)]), person_moves, is_fire=False)
    
        dest_fire, dest_move = fire_moves[-1][-1], person_moves[-1][-1]
        if dest_move < 0: return -1
        if dest_fire < 0: return 10**9
        if dest_fire == dest_move: return 0

        diff = dest_fire - dest_move
        if m > 1 and n > 1:
            path1, path2 = person_moves[-1][-2], person_moves[-2][-1]
            diff1, diff2 = fire_moves[-1][-2] - path1, fire_moves[-2][-1] - path2
            if path1 >= 0 and path2 >= 0 and (diff1 > diff or diff2 > diff):
                return diff

        return diff - 1

        """
        m, n = map(len, (grid, grid[0]))
        inf = 10**10
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fires = [(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 1]
        grid = [[inf if a < 2 else -1 for a in r] for r in grid]

        def bfs(queue, seen):
            for i, j, t in queue:
                if seen[i][j] < inf: continue
                seen[i][j] = t
                for di, dj in d:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and seen[x][y] >= inf and grid[x][y] > t + 1:
                        queue.append((x, y, t + 1))

        def die(t):
            seen = [[inf + 10] * n for _ in range(m)]
            bfs([(0, 0, t)], seen)
            return seen[-1][-1] > grid[-1][-1]

        bfs(fires, grid)
        grid[-1][-1] += 1
        return bisect.bisect_left(range(10**9 + 1), True, key=die) - 1
        """

        
# @lc code=end

