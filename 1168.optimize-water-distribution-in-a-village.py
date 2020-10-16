#
# @lc app=leetcode id=1168 lang=python3
#
# [1168] Optimize Water Distribution in a Village
#
# https://leetcode.com/problems/optimize-water-distribution-in-a-village/description/
#
# algorithms
# Hard (59.28%)
# Likes:    201
# Dislikes: 6
# Total Accepted:    5.3K
# Total Submissions: 8.9K
# Testcase Example:  '3\n[1,2,2]\n[[1,2,1],[2,3,1]]'
#
# There are n houses in a village. We want to supply water for all the houses
# by building wells and laying pipes.
# 
# For each house i, we can either build a well inside it directly with cost
# wells[i], or pipe in water from another well to it. The costs to lay pipes
# between houses are given by the array pipes, where each pipes[i] = [house1,
# house2, cost] represents the cost to connect house1 and house2 together using
# a pipe. Connections are bidirectional.
# 
# Find the minimum total cost to supply water to all houses.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation: 
# The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the first house with cost 1 and
# connect the other houses to it with cost 2 so the total cost is 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10000
# wells.length == n
# 0 <= wells[i] <= 10^5
# 1 <= pipes.length <= 10000
# 1 <= pipes[i][0], pipes[i][1] <= n
# 0 <= pipes[i][2] <= 10^5
# pipes[i][0] != pipes[i][1]
# 
# 
#

# @lc code=start
from collections import defaultdict
import heapq

# Treat the wells as pipes from a virtual node 0.

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Minimum Spanning Tree
        # graph = defaultdict(list)
        # for u, v, w in pipes:
        #     graph[u].append([w, u, v])
        #     graph[v].append([w, v, u])

        # for i in range(n):
        #     graph[0].append([wells[i], 0, i + 1])

        # visited, edges = {0}, graph[0]
        # heapq.heapify(edges)
        # res = 0

        # while len(visited) < n + 1 and edges:
        #     w, u, v = heapq.heappop(edges)
        #     if v not in visited:
        #         res += w
        #         visited.add(v)
        #         for edge in graph[v]:
        #             if edge[2] not in visited:
        #                 heapq.heappush(edges, edge)

        # return res



        # Time  complexity: O(ElogE)
        # Space complexity: O(N)
        uf = {i: i for i in range(n + 1)}

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]

        res = 0
        for c, x, y in sorted(w + p):
            x, y = map(find, (x, y))
            if x != y:
                uf[x] = y
                res += c
                n -= 1

            if n == 0:
                return res


        
# @lc code=end

