#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Time  complexity: O(M x logN + N)
        # Space complexity: O(N + M)
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [float("inf")] * n
            ways = [0] * n
            minHeap = [(0, src)] # dist, src
            dist[src] = 0
            ways[src] = 1

            while minHeap:
                d, u = heapq.heappop(minHeap)
                if dist[u] < d: continue
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heapq.heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % (10**9 + 7)

            return ways[n - 1]

        return dijkstra(0)
        
# @lc code=end

