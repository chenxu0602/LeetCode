#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from heapq import heappush, heappop
from itertools import product

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        m, n = map(len, (moveTime, moveTime[0]))
        directions = [-1, 0, 1, 0, -1]
        heap = [(0, 0, 0)]
        unvisited = set(product(range(m), range(n)))

        while heap:
            time, x, y = heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return time

            for i in range(4):
                dx, dy = directions[i], directions[i + 1]
                X, Y = x + dx, y + dy

                if (X, Y) in unvisited:
                    t = max(time, moveTime[X][Y]) + 1
                    heappush(heap, (t, X, Y))
                    unvisited.remove((X, Y))
            


        
# @lc code=end

