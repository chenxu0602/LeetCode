#
# @lc app=leetcode id=2608 lang=python3
#
# [2608] Shortest Cycle in a Graph
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        # Assume a node is root and apply bfs search,
        # where we recode the:
        # dis[i] is the distance from root to i
        # fa[i] is the father of i
        # If two points met up and they are not father-son relation,
        # they met in a cycle.
        # The distance of circly is smaller or equal than dis[i] + dis[j] + 1.

        # Time  complexity: O(n^2)
        # Space complexity: O(edges + n)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            dist = [float("inf")] * n
            dist[node] = 0
            bfs = [node]
            mn = float("inf")
            for i in bfs:
                for j in graph[i]:
                    if dist[j] == float("inf"):
                        dist[j] = dist[i] + 1
                        bfs.append(j)
                    elif dist[i] <= dist[j]:
                        mn = min(mn, dist[i] + dist[j] + 1)
            return mn

        res = min(map(dfs, range(n)))
        return res if res < float("inf") else -1
        
# @lc code=end

