#
# @lc app=leetcode id=1928 lang=python3
#
# [1928] Minimum Cost to Reach Destination in Time
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        n = len(passingFees)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        times = {}
        queue = [(passingFees[0], 0, 0)]

        while queue:
            cost, node, time = heapq.heappop(queue)

            if time > maxTime: continue

            if node == n - 1: return cost

            if node not in times or times[node] > time:
                times[node] = time
                for nei, w in graph[node]:
                    heapq.heappush(queue, (passingFees[nei] + cost, nei, time + w))

        return -1




        
        
# @lc code=end

