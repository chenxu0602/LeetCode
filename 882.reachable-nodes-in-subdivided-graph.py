#
# @lc app=leetcode id=882 lang=python3
#
# [882] Reachable Nodes In Subdivided Graph
#
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/
#
# algorithms
# Hard (38.60%)
# Likes:    109
# Dislikes: 101
# Total Accepted:    4K
# Total Submissions: 10.2K
# Testcase Example:  '[[0,1,10],[0,2,1],[1,2,2]]\n6\n3'
#
# Starting with an undirected graph (the "original graph") with nodes from 0 to
# N-1, subdivisions are made to some of the edges.
# 
# The graph is given as follows: edges[k] is a list of integer pairs (i, j, n)
# such that (i, j) is an edge of the original graph,
# 
# and n is the total number of new nodes on that edge. 
# 
# Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1,
# x_2, ..., x_n) are added to the original graph,
# 
# and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n),
# (x_n, j) are added to the original graph.
# 
# Now, you start at node 0 from the original graph, and in each move, you
# travel along one edge. 
# 
# Return how many nodes you can reach in at most M moves.
# 
# 
# 
# Example 1:
# 
# 
# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
# Output: 13
# Explanation: 
# The nodes that are reachable in the final graph after M = 6 moves are
# indicated below.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= edges.length <= 10000
# 0 <= edges[i][0] < edges[i][1] < N
# There does not exist any i != j for which edges[i][0] == edges[j][0] and
# edges[i][1] == edges[j][1].
# The original graph has no parallel edges.
# 0 <= edges[i][2] <= 10000
# 0 <= M <= 10^9
# 1 <= N <= 3000
# A reachable node is a node that can be travelled to using at most M moves
# starting from node 0.
# 
# 
# 
# 
# 
# 
#
from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            ans += 1

            for nei, weight in graph[node].items():
                v = min(weight, M - d)
                used[node, nei] = v

                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans


        

