#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n = map(len, (maze, maze[0]))
        reached = lambda p, q: (not p == x or not q == y) and (p == 0 or q == 0 or p == m - 1 or q == n - 1)
        directions = [1, 0, -1, 0, 1]

        queue = deque([(x, y, 0)])
        while queue:
            r, c, ans = queue.popleft()
            for i in range(4):
                nr, nc = r + directions[i], c + directions[i + 1]
                if nr < 0 or nc < 0 or nr == m or nc == n or maze[nr][nc] == '+':
                    continue

                if reached(nr, nc):
                    return ans + 1

                maze[nr][nc] = '+'
                queue.append((nr, nc, ans + 1))

        return -1
        
# @lc code=end

