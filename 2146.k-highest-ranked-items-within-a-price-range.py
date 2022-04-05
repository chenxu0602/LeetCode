#
# @lc app=leetcode id=2146 lang=python3
#
# [2146] K Highest Ranked Items Within a Price Range
#

# @lc code=start
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        ans = []
        dq = deque([(start[0], start[1], 0)])
        seen = set([(start[0], start[1])])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m, n = map(len, (grid, grid[0]))

        while dq:
            x, y, d = dq.popleft()

            if pricing[0] <= grid[x][y] <= pricing[1]:
                ans.append([d, grid[x][y], x, y])

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] > 0:
                    seen.add((nx, ny))
                    dq.append((nx, ny, d + 1))

        ans.sort()

        return [x[2:] for x in ans[:k]]

        
# @lc code=end

