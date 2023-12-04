#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (39.29%)
# Likes:    2257
# Dislikes: 76
# Total Accepted:    120.7K
# Total Submissions: 307.2K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each flight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#

# @lc code=start
import heapq
from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Dijkstra's Algorithm
        # Time  complexity: O(V^2 x logV)
        # Space complexity: O(V^2)
        adj_matrix = [[0] * n for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w

        distances = [float("inf")] * n
        current_stops = [float("inf")] * n
        distances[src], current_stops[src] = 0, 0

        minHeap = [(0, 0, src)]

        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)
            if node == dst: return cost
            if stops == K + 1: continue

            # Examine and relax all neighboring edges if possible 
            for nei in range(n):
                if adj_matrix[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_matrix[node][nei]
                    if dU + wUV < dV or stops + 1 < current_stops[nei]:
                        distances[nei] = dU + wUV
                        current_stops[nei] = stops + 1
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))

        return -1 if distances[dst] == float("inf") else distances[dst]

        # graph = defaultdict(dict)
        # for u, v, w in flights:
        #     graph[u][v] = w

        # best = {}
        # pq = [(0, 0, src)]
        # while pq:
        #     cost, k, place = heapq.heappop(pq)
        #     if k > K + 1 or cost > best.get((k, place), float("inf")) :
        #         continue
        #     if place == dst: return cost

        #     for nei, wt in graph[place].items():
        #         newcost = cost + wt
        #         if newcost < best.get((k + 1, nei), float("inf")):
        #             heapq.heappush(pq, (newcost, k + 1, nei))
        #             best[k + 1, nei] = newcost

        # return -1


        # pq = [(0, src, K + 1)]
        # graph = defaultdict(dict)

        # for s, d, c in flights:
        #     graph[s][d] = c

        # while pq:
        #     cost, s, k = heapq.heappop(pq)
        #     if s == dst: return cost
        #     if k:
        #         for d in graph[s]:
        #             heapq.heappush(pq, (cost + graph[s][d], d, k - 1))

        # return -1



        # Breadth First Search
        # Time  complexity: O(E x K)
        # Space complexity: O(V^2 + V x K)
        # adj_matrix = [[0] * n for _ in range(n)]
        # for s, d, w in flights: adj_matrix[s][d] = w

        # distances = {}
        # distances[(src, 0)] = 0

        # bfsQ, stops, ans = deque([src]), 0, float("inf")

        # # Iterate until we exhaust K+1 levels or the queue gets empty
        # while bfsQ and stops < K + 1:
        #     length = len(bfsQ)
        #     for _ in range(length):
        #         node = bfsQ.popleft()

        #         # Loop over neighbors of popped node
        #         for nei in range(n):
        #             if adj_matrix[node][nei] > 0:
        #                 dU = distances.get((node, stops), float("inf"))
        #                 dV = distances.get((nei, stops + 1), float("inf"))
        #                 wUV = adj_matrix[node][nei]

        #                 if stops == K and nei != dst:
        #                     continue

        #                 if dU + wUV < dV:
        #                     distances[nei, stops + 1] = dU + wUV
        #                     bfsQ.append(nei)

        #                     if nei == dst:
        #                         ans = min(ans, dU + wUV)

        #     stops += 1

        # return -1 if ans == float("inf") else ans

        
        # Bellman-Ford
        # Time  complexity: O(K x E)
        # Space compleixty: O(V)
        # We use two arrays for storing distances and keep swapping
        # between them to save on the memory
        # distances = [[float("inf")] * n for _ in range(2)]
        # distances[0][src] = distances[1][src] = 0

        # # K + 1 iterations of Bellman Ford
        # for iterations in range(K + 1):
        #     # Iterate over all the edges
        #     for s, d, wUV in flights:
        #         # Current distance of node "s" from src
        #         dU = distances[1 - iterations & 1][s]
        #         # Current distance of node "d" from src
        #         # Note that this will port existing values as
        #         # well from the "previous" array if they didn't already exist
        #         dV = distances[iterations & 1][d]
        #         # Relax the edge if possible
        #         if dU + wUV < dV:
        #             distances[iterations & 1][d] = dU + wUV

        # return -1 if distances[K & 1][dst] == float("inf") else distances[K & 1][dst]
# @lc code=end

