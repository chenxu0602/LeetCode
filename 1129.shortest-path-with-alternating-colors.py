#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (36.02%)
# Likes:    140
# Dislikes: 6
# Total Accepted:    5.7K
# Total Submissions: 15.3K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this
# graph, each edge is either red or blue, and there could be self-edges or
# parallel edges.
# 
# Each [i, j] in red_edges denotes a red directed edge from node i to node j.
# Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i
# to node j.
# 
# Return an array answer of length n, where each answer[X] is the length of the
# shortest path from node 0 to node X such that the edge colors alternate along
# the path (or -1 if such a path doesn't exist).
# 
# 
# Example 1:
# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
# Example 2:
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
# Example 3:
# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
# Example 4:
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
# Example 5:
# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n
# 
#

# @lc code=start
import math
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        """
        G = [[[], []] for _ in range(n)]
        for i, j in red_edges:
            G[i][0].append(j)
        for i, j in blue_edges:
            G[i][1].append(j)

        res = [[0, 0]] + [[n*2, n*2] for i in range(n-1)]
        bfs = [[0, 0], [0, 1]]

        for i, c in bfs:
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1-c] + 1
                    bfs.append([j, 1-c])
            
        return [x if x < n*2 else -1 for x in map(min, res)]
        """

        graph = {i: [[], []] for i in range(n)}
        for i, j in red_edges:
            graph[i][0].append(j)
        for i, j in blue_edges:
            graph[i][1].append(j)

        res = [math.inf for _ in range(n)]
        res[0] = 0
        min_len = 0

        queue = deque()
        queue.append((0, 'r'))
        queue.append((0, 'b'))

        seen = set()

        while queue:
            level_size = len(queue)
            min_len += 1

            for _ in range(level_size):
                node, color = queue.popleft()

                if (node, color) not in seen:
                    seen.add((node, color))

                    if color == 'r':
                        for child in graph[node][1]:
                            queue.append((child, 'b'))
                            res[child] = min(min_len, res[child])
                    
                    if color == 'b':
                        for child in graph[node][0]:
                            queue.append((child, 'r'))
                            res[child] = min(min_len, res[child])

        for i in range(n):
            if res[i] == math.inf:
                res[i] = -1

        return res



        
# @lc code=end

