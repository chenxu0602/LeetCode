#
# @lc app=leetcode id=2596 lang=python3
#
# [2596] Check Knight Tour Configuration
#

# @lc code=start
from collections import defaultdict
from itertools import product

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        """
        n, d = len(grid), defaultdict(tuple)
        notLegal = lambda x, y: {abs(x[0] - y[0]), abs(x[1] - y[1])} != {1, 2}

        for r, c in product(range(n), range(n)):
            d[grid[r][c]] = (r, c)

        prev, cnt = (0, 0), 1
        while cnt < n * n:
            curr = d[cnt]

            if notLegal(prev, curr):
                return False

            cnt += 1
            prev = curr

        return True
        """

        n, visited = len(grid), set()

        def dfs(r, c, move):
            if r < 0 or r >= n or c < 0 or c >= n or (r, c) in visited or grid[r][c] != move:
                return

            visited.add((r, c))

            for dr, dc in (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1):
                nr, nc = r + dr, c + dc
                dfs(nr, nc, move + 1)

        dfs(0, 0, 0) 
        return len(visited) == n * n
        
# @lc code=end

