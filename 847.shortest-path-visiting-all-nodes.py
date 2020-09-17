#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (47.81%)
# Likes:    349
# Dislikes: 38
# Total Accepted:    9.8K
# Total Submissions: 20.2K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is
# given as graph.
# 
# graph.length = N, and j != i is in the list graph[i] exactly once, if and
# only if nodes i and j are connected.
# 
# Return the length of the shortest path that visits every node. You may start
# and stop at any node, you may revisit nodes multiple times, and you may reuse
# edges.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# 
# Example 2:
# 
# 
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= graph.length <= 12
# 0 <= graph[i].length < graph.length
# 
# 
#
class Node(object):
    def __init__(self, nodeId, visitedSoFar):
        self.id = nodeId
        self.journal = visitedSoFar

    def __eq__(self, other):
        return self.id == other.id and self.journal == other.journal

    def __repr__(self):
        return "Node({}, {})".format(self.id, bin(self.journal)[2:])

    def __hash__(self):
        return hash((self.id, self.journal))

from collections import defaultdict, deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        # N = len(graph)

        # q = deque(Node(i, 1 << i) for i in range(N))

        # distanceToThisNode = defaultdict(lambda: N * N)

        # for i in range(N):
        #     distanceToThisNode[Node(i, 1 << i)] = 0

        # endJournal = (1 << N) - 1

        # while q:
        #     node = q.popleft()
        #     dist = distanceToThisNode[node]

        #     if node.journal == endJournal:
        #         return dist

        #     neighboring_cities = graph[node.id]

        #     for city in neighboring_cities:
        #         newJournal = node.journal | (1 << city)

        #         neighbor_node = Node(city, newJournal)

        #         if dist + 1 < distanceToThisNode[neighbor_node]:
        #             distanceToThisNode[neighbor_node] = dist + 1
        #             q.append(neighbor_node)
        # return -1


        # Breadth First Search
        # Time  complexity: O(N x 2^N)
        # Space complexity: O(N x 2^N)
        N = len(graph)
        queue = deque((1 << x, x) for x in range(N))
        dist = defaultdict(lambda: N * N)
        for x in range(N): dist[1 << x, x] = 0

        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2 ** N - 1:
                return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))


        # Dynamic Programming
        # Time  complexity: O(N x 2^N)
        # Space complexity: O(N x 2^N)
        # N = len(graph)
        # dist = [[float("inf")] * N for i in range(1 << N)]
        # for x in range(N): dist[1 << x][x] = 0

        # for cover in range(1 << N):
        #     repeat = True
        #     while repeat:
        #         repeat = False
        #         for head, d in enumerate(dist[cover]):
        #             for nei in graph[head]:
        #                 cover2 = cover | (1 << nei)
        #                 if d + 1 < dist[cover2][nei]:
        #                     dist[cover2][nei] = d + 1
        #                     if cover == cover2:
        #                         repeat = True

        # return min(dist[2 ** N - 1])

            
        

