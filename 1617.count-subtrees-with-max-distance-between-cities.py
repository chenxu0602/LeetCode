#
# @lc app=leetcode id=1617 lang=python3
#
# [1617] Count Subtrees With Max Distance Between Cities
#
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/description/
#
# algorithms
# Hard (62.98%)
# Likes:    126
# Dislikes: 20
# Total Accepted:    3.6K
# Total Submissions: 5.8K
# Testcase Example:  '4\n[[1,2],[2,3],[2,4]]'
#
# There are n cities numbered from 1 to n. You are given an array edges of size
# n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities
# ui and vi. There exists a unique path between each pair of cities. In other
# words, the cities form a tree.
# 
# A subtree is a subset of cities where every city is reachable from every
# other city in the subset, where the path between each pair passes through
# only the cities from the subset. Two subtrees are different if there is a
# city in one subtree that is not present in the other.
# 
# For each d from 1 to n-1, find the number of subtrees in which the maximum
# distance between any two cities in the subtree is equal to d.
# 
# Return an array of size n-1 where the d^th element (1-indexed) is the number
# of subtrees in which the maximum distance between any two cities is equal to
# d.
# 
# Notice that the distance between the two cities is the number of edges in the
# path between them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, edges = [[1,2],[2,3],[2,4]]
# Output: [3,4,0]
# Explanation:
# The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
# The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max
# distance of 2.
# No subtree has two nodes where the max distance between them is 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, edges = [[1,2]]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: n = 3, edges = [[1,2],[2,3]]
# Output: [2,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 15
# edges.length == n-1
# edges[i].length == 2
# 1 <= ui, vi <= n
# All pairs (ui, vi) are distinct.
# 
#

# @lc code=start
from collections import defaultdict, deque
import itertools

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # Using Floyd-Warshall algorithm to calculate minimum distance between any node to any other node.
        # Since n <= 15, there is a maximum 2^15 subset of cities numbered from 1 to n.
        # Time  complexity: O(2^n x n^2)
        # Space complexity: O(n^2)
        # def maxDistance(state): # return: maximum distance between any two cities in our subset. O(n^2)
        #     cntEdge, cntCity, maxDist = 0, 0, 0
        #     for i in range(n):
        #         if state >> i & 1 == 0:
        #             continue # Skip if city `i` not in our subset
        #         cntCity += 1
        #         for j in range(i + 1, n):
        #             if state >> j & 1 == 0:
        #                 continue # Skip if city `j` not in our subset
        #             cntEdge += dist[i][j] == 1
        #             maxDist = max(maxDist, dist[i][j])
        #     if cntEdge != cntCity - 1:
        #         return 0 # Subset form an invalid subtree!
        #     return maxDist

        # INF = n # Since cities form a tree so maximum distance between 2 cities always < n
        # dist = [[INF] * n for _ in range(n)]
        # for u, v in edges:
        #     dist[u - 1][v - 1] = dist[v - 1][u - 1] = 1

        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # ans = [0] * (n - 1)
        # for state in range(1, 1 << n):
        #     d = maxDistance(state)
        #     if d > 0:
        #         ans[d - 1] += 1
        # return ans


        # Bitmask + BFS every cities
        # Time  complexity: O(2^n x n^2)
        # Space complexity: O(n^2)
        def bfs(src, cities):
            visited = {src}
            q = deque([(src, 0)]) # Pair of (vertex, distance)
            farthestDist = 0 # Farthest distance from src to other nodes
            while len(q) > 0:
                u, d = q.popleft()
                farthestDist = d
                for v in graph[u]:
                    if v not in visited and v in cities:
                        visited.add(v)
                        q.append((v, d + 1))
            return farthestDist, visited

        def maxDistance(state): # return: maximum distance between any two cities in our subset. O(n^2)
            cities = set()
            for i in range(n):
                if state >> i & 1 == 1:
                    cities.add(i)

            ans = 0
            for i in cities:
                farthestDist, visited = bfs(i, cities)
                if len(visited) < len(cities):
                    return 0 # Can't visit all nodes of the tree -> Invalid tree
                ans = max(ans, farthestDist)
            return ans

        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        ans = [0] * (n - 1)
        for state in range(1, 1 << n):
            d = maxDistance(state)
            if d > 0:
                ans[d - 1] += 1
        return ans



        # Bitmask + Diamter of the tree (BFS 2 times)
        # Time  complexity: O(2^n x n)
        # Space complexity: O(n^2)
        # def bfs(src, cities):
        #     visited = {src}
        #     q = deque([(src, 0)]) # Pair of (vertex, distance)
        #     farthestNode, farthestDist = -1, 0
        #     while len(q) > 0:
        #         farthestNode, farthestDist = u, d = q.popleft()
        #         for v in graph[u]:
        #             if v not in visited and v in cities:
        #                 visited.add(v)
        #                 q.append((v, d + 1))
        #     return farthestNode, farthestDist, visited

        # def diameterOfTree(cities):
        #     anyNode = cities.pop()
        #     cities.add(anyNode)
        #     farthestNode, _, visited = bfs(anyNode, cities)
        #     if len(visited) < len(cities):
        #         return 0 # Can't visit all nodes of the tree -> Invalid tree
        #     _, dist, _ = bfs(farthestNode, cities)
        #     return dist

        # def maxDistance(state): # return: maximum distance between any two cities in our subset. O(n)
        #     cities = set()
        #     for i in range(n):
        #         if state >> i & 1 == 1:
        #             cities.add(i)
        #     return diameterOfTree(cities)
                
        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u - 1].append(v - 1)
        #     graph[v - 1].append(u - 1)

        # ans = [0] * (n - 1)
        # for state in range(1, 1 << n):
        #     d = maxDistance(state)
        #     if d > 0:
        #         ans[d - 1] += 1
        # return ans


        # Use Floyd-Warshall Algorithm to find all shortest paths.
        # Brute force all possible subsets and count subtrees with diameter d.
        # Time  complexity: O(2^n x n^2)
        # Space complexity: O(n^2)
        # dist = [[float("inf")] * n for _ in range(n)]
        # for u, v in edges:
        #     dist[u - 1][v - 1] = dist[v - 1][u - 1] = 1

        # for k, i, j in itertools.permutations(range(n), 3):
        #     dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # ans = [0] * (n - 1)
        # for k in range(2, n + 1):
        #     for s in itertools.combinations(range(n), k):
        #         e = sum(dist[i][j] for i, j in itertools.combinations(s, 2) if dist[i][j] == 1) 
        #         d = max(dist[i][j] for i, j in itertools.combinations(s, 2))
        #         if e == k - 1:
        #             ans[d - 1] += 1

        # return ans
        
# @lc code=end

