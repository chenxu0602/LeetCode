#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
import heapq, bisect

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = map(len, (grid, grid[0]))
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        order = []

        while len(heap) > 0:
            curr, i, j = heapq.heappop(heap)
            order.append(curr)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))

        maxYet = -1
        for i in range(len(order)):
            maxYet = max(maxYet, order[i])
            order[i] = maxYet

        res = []
        for q in queries:
            res.append(bisect.bisect_left(order, q))

        return res
        
# @lc code=end

