#
# @lc app=leetcode id=2203 lang=python3
#
# [2203] Minimum Weighted Subgraph With the Required Paths
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # Time complexity:  O(nxlogE)
        # Space complexity: O(n)

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for a, b, w in edges:
            graph1[a].append((b, w))
            graph2[b].append((a, w))

        def Dijkstra(graph, K):
            q, t = [(0, K)], {}
            while q:
                time, node = heapq.heappop(q)
                if node not in t:
                    t[node] = time
                    for v, w in graph[node]:
                        heapq.heappush(q, (time + w, v))

            return [t.get(i, float("inf")) for i in range(n)]

        arr1 = Dijkstra(graph1, src1)
        arr2 = Dijkstra(graph1, src2)
        arr3 = Dijkstra(graph2, dest)

        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])

        return ans if ans != float("inf") else -1

        
# @lc code=end

