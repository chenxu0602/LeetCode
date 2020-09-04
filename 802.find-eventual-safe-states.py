#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#
# https://leetcode.com/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (48.83%)
# Likes:    839
# Dislikes: 160
# Total Accepted:    41.4K
# Total Submissions: 84.3K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# In a directed graph, we start at some node and every turn, walk along a
# directed edge of the graph.  If we reach a node that is terminal (that is, it
# has no outgoing directed edges), we stop.
# 
# Now, say our starting node is eventually safe if and only if we must
# eventually walk to a terminal node.  More specifically, there exists a
# natural number K so that for any choice of where to walk, we must have
# stopped at a terminal node in less than K steps.
# 
# Which nodes are eventually safe?  Return them as an array in sorted order.
# 
# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the
# length of graph.  The graph is given in the following form: graph[i] is a
# list of labels j such that (i, j) is a directed edge of the graph.
# 
# 
# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Here is a diagram of the above graph.
# 
# 
# 
# 
# 
# Note:
# 
# 
# graph will have length at most 10000.
# The number of edges in the graph will not exceed 32000.
# Each graph[i] will be a sorted list of different integers, chosen within the
# range [0, graph.length - 1].
# 
# 
#

# @lc code=start
from collections import defaultdict, deque
from functools import lru_cache

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Reverse Edges
        # Time  complexity: O(N + E), where N is the number of nodes in the given graph,
        # and E is the total number of edges.
        # Space complexity: O(N) in additional space complexity.
        # N = len(graph)
        # safe = [False] * N

        # graph = list(map(set, graph))
        # rgraph = [set() for _ in range(N)]
        # q = deque()

        # for i, js in enumerate(graph):
        #     if not js:
        #         q.append(i)
        #     for j in js:
        #         rgraph[j].add(i)

        # while q:
        #     j = q.popleft()
        #     safe[j] = True
        #     for i in rgraph[j]:
        #         graph[i].remove(j)
        #         if len(graph[i]) == 0:
        #             q.append(i)

        # return [i for i, v in enumerate(safe) if v]
        

        # Depth-First Search
        # Time  complexity: O(N + E), where N is the number of nodes in the given graph,
        # and E is the total number of edges.
        # Space complexity: O(N) in additional space complexity.
        WHITE, GRAY, BLACK, = 0, 1, 2
        color = defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False

            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))
# @lc code=end

