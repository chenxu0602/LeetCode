#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
# https://leetcode.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (45.78%)
# Likes:    985
# Dislikes: 127
# Total Accepted:    79.5K
# Total Submissions: 173.5K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# Given an undirected graph, return true if and only if it is bipartite.
# 
# Recall that a graph is bipartite if we can split it's set of nodes into two
# independent subsets A and B such that every edge in the graph has one node in
# A and another node in B.
# 
# The graph is given in the following form: graph[i] is a list of indexes j for
# which the edge between nodes i and j exists.  Each node is an integer between
# 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i]
# does not contain i, and it doesn't contain any element twice.
# 
# 
# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# 
# 
# 
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent
# subsets.
# 
# 
# 
# 
# Note:
# 
# 
# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in
# graph[j].
# 
# 
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Coloring by Depth-First Search
        # Time  complexity: O(N + E), where N is the number of nodes in the graph,
        # and E is the number of edges.
        # Space complexity: O(N)
        # color = {}
        # for node in range(len(graph)):
        #     if node not in color:
        #         stack = [node]
        #         color[node] = 0
        #         while stack:
        #             node = stack.pop()
        #             for nei in graph[node]:
        #                 if nei not in color:
        #                     stack.append(nei)
        #                     color[nei] = color[node] ^ 1
        #                 elif color[nei] == color[node]:
        #                     return False

        # return True


        color = {}
        def dfs(x, c):
            if x in color:
                return c == color[x]
            color[x] = c
            return all(dfs(y, 1 - c) for y in graph[x])

        return all(dfs(x, 0) for x in range(len(graph)) if x not in color)


        
# @lc code=end

