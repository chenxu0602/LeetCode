#
# @lc app=leetcode id=3342 lang=python3
#
# [3342] Find Minimum Time to Reach Last Room II
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        m, n = map(len, (moveTime, moveTime[0]))
        onGrid = lambda x, y: 0 <= x < m and 0 <= y < n
        directions = [-1, 0, 1, 0, -1]
        heap = [(0, 0, 0, 1)]
        seen = {(0, 0)}

        while heap:
            time, x, y, step = heappop(heap)

            if (x, y) == (m - 1, n - 1):
                return time

            for i in range(4):
                dx, dy = directions[i], directions[i + 1]
                X, Y = x + dx, y + dy

                if onGrid(X, Y) and (X, Y) not in seen:
                    t = max(time, moveTime[X][Y]) + step
                    heappush(heap, (t, X, Y, 3 - step))
                    seen.add((X, Y))

        
# @lc code=end

