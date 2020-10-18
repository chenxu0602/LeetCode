#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (48.29%)
# Likes:    575
# Dislikes: 53
# Total Accepted:    28.1K
# Total Submissions: 58.3K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] = [a, b]
# represents a connection between servers a and b. Any server can reach any
# other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
# 
# 
#

# @lc code=start

from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # An edge is a critical connection, if and only if it is not in a cycle.
        # if we know how to find cycles, and discard all edges in the cycles, then the remaining connections are a complete collection of critical connections.
        # Only the nodes on the current DFS path have non-special ranks. 
        # if a node is not visited yet, it has a special rank -2; if we've fully completed the visit of a node, it has a special rank n.
        # Time  complexity: O(E + V)
        # Space complexity: O(graph) + O(rank) + O(connections) = O(E)
        # def makeGraph(connections):
        #     graph = defaultdict(list)
        #     for u, v in connections:
        #         graph[u].append(v)
        #         graph[v].append(u)
        #     return graph

        # graph = makeGraph(connections)
        # connections = set(map(tuple, (map(sorted, connections))))
        # rank = [-2] * n

        # def dfs(node, depth):
        #     if rank[node] >= 0:
        #         return rank[node]
        #     rank[node] = depth
        #     min_back_depth = n

        #     for nei in graph[node]:
        #         if rank[nei] == depth - 1:
        #             continue
        #         back_depth = dfs(nei, depth + 1)
        #         if back_depth <= depth:
        #             connections.discard(tuple(sorted((node, nei))))

        #         min_back_depth = min(min_back_depth, back_depth)

        #     rank[node] = n
        #     return min_back_depth

        # dfs(0, 0)
        # return list(connections)


        graph = [[] for _ in range(n)] # vertex i ==> [its neighbors]
        currentRank = 0
        lowestRank = [i for i in range(n)] # lowestRank[i] represents the lowest order of vertex that can reach this vertex i
        visited = [False for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        prevVertex = -1
        currentVertex = 0

        def dfs(currentRank, prevVertex, currentVertex):
            visited[currentVertex] = True
            lowestRank[currentVertex] = currentRank

            for nextVertex in graph[currentVertex]:
                if nextVertex == prevVertex:
                    continue
                if not visited[nextVertex]:
                    dfs(currentRank + 1, currentVertex, nextVertex)

                lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])

                if lowestRank[nextVertex] >= currentRank + 1:
                    res.append([currentVertex, nextVertex]) 

        dfs(currentRank, prevVertex, currentVertex)
        return res
        
# @lc code=end

