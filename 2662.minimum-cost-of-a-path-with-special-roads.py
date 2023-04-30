#
# @lc app=leetcode id=2662 lang=python3
#
# [2662] Minimum Cost of a Path With Special Roads
#

# @lc code=start
import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:

        # Dijkstra's Algorithms

        """
        specialRoads = [[a, b, c, d, x] for a, b, c, d, x in specialRoads if x < abs(a - c) + abs(b - d)]
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while len(heap) > 0:
            cur_d, x, y = heapq.heappop(heap)
            for a, b, c, d, cost in specialRoads:
                if dist.get((c, d), float("inf")) > cur_d + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = cur_d + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))

            res = abs(target[0] - start[0]) + abs(target[1] - start[1])

        for a, b, c, d, cost in specialRoads:
            res = min(res, dist.get((c, d), float("inf")) + abs(target[0] - c) + abs(target[1] -d))

        return res
        """

        mp = defaultdict(list, {tuple(target): [(0, 0, 0)]})
        for a, b, c, d, cost in specialRoads:
            mp[a, b].append((c, d, cost))

        dist = defaultdict(lambda: float("inf"))
        dist[tuple(start)] = 0
        heap = [(0, *start)]

        while heap:
            cur_d, a, b = heapq.heappop(heap)
            if [a, b] == target: return cur_d
            for c, d, cost in mp[a, b]:
                if cur_d + cost < dist[c, d]:
                    dist[c, d] = cur_d + cost
                    heapq.heappush(heap, (cur_d + cost, c, d))

            for a1, b1 in mp:
                direct_d = cur_d + abs(a - a1) + abs(b - b1)
                if direct_d < dist[a1, b1]:
                    dist[a1, b1] = direct_d
                    heapq.heappush(heap, (direct_d, a1, b1))

        
# @lc code=end

