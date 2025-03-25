#
# @lc app=leetcode id=3313 lang=python3
#
# [3313] Find the Last Marked Nodes in Tree
#

# @lc code=start
from collections import deque

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:

        n = len(edges) + 1

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u] += v,
            adj[v] += u,

        def bfs(start):
            queue = deque([start])
            visited = [-1] * n
            visited[start] = True
            last_node = start
            max_depth = 0

            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = visited[node] + 1
                        queue.append(neighbor)
                        if visited[neighbor] > max_depth:
                            max_depth = visited[neighbor]
                            last_node = neighbor

            return last_node, visited
                        

        farthest1, _ = bfs(0)
        farthest2, dist1 = bfs(farthest1)
        _, dist2 = bfs(farthest2)

        result = []
        for i in range(n):
            if dist1[i] > dist2[i]:
                result += farthest1,
            else:
                result += farthest2,

        return result


        # def bfs(start):
        #     visited = set([start])
        #     queue = deque([start])
        #     last_node = -1
        #     dist = [0] * n
        #     level = 0
        #     while queue:
        #         for _ in range(len(queue)):
        #             node = queue.popleft()
        #             dist[node] = level
        #             last_node = node
        #             for nei in adj_list[node]:
        #                 if nei not in visited:
        #                     visited.add(nei)
        #                     queue.append(nei)
        #         level += 1
        #     return last_node, dist

        # n = len(edges) + 1
        # adj_list = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj_list[u] += v,
        #     adj_list[v] += u,

        # a, _ = bfs(0)
        # b, a_n = bfs(a)
        # _, b_n = bfs(b)

        # last_nodes = []
        # for i in range(n):
        #     last_nodes += a if a_n[i] > b_n[i] else b,

        # return last_nodes


        
# @lc code=end

