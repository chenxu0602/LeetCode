#
# @lc app=leetcode id=3243 lang=python3
#
# [3243] Shortest Distance After Road Addition Queries I
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        """
        # Bellman Ford
        def bellman(adj):
            m = len(adj)
            dist = [float('inf')] * m
            dist[0] = 0

            for u in range(m):
                for v in adj[u]:
                    if dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1

            return dist[-1]


        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i] += i + 1,

        res = []
        for i, j in queries:
            adj[i] += j,
            res += bellman(adj),

        return res
        """


        # Dijkstra
        def dijkstra(graph, m):
            dist = [float('inf')] * m
            dist[0] = 0
            heap = [(0, 0)]

            while heap:
                d, u = heappop(heap)
                if d > dist[u]: continue
                for v, w in graph[u]:
                    d2 = d + w
                    if d2 < dist[v]:
                        dist[v] = d2
                        heappush(heap, (d2, v))

            return dist[-1]


        graph = {i : [] for i in range(n)}
        for i in range(n - 1):
            graph[i] += (i + 1, 1),

        res = []
        for u, v in queries:
            graph[u] += (v, 1),
            dist = dijkstra(graph, n)
            res += dist,

        return res


        


        
# @lc code=end

