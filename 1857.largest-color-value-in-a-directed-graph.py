#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
#
# algorithms
# Hard (35.27%)
# Likes:    219
# Dislikes: 8
# Total Accepted:    4.5K
# Total Submissions: 12.9K
# Testcase Example:  '"abaca"\n[[0,1],[0,2],[2,3],[3,4]]'
#
# There is a directed graph of n colored nodes and m edges. The nodes are
# numbered from 0 to n - 1.
# 
# You are given a string colors where colors[i] is a lowercase English letter
# representing the color of the i^th node in this graph (0-indexed). You are
# also given a 2D array edges where edges[j] = [aj, bj] indicates that there is
# a directed edge from node aj to node bj.
# 
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
# such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
# color value of the path is the number of nodes that are colored the most
# frequently occurring color along that path.
# 
# Return the largest color value of any valid path in the given graph, or -1 if
# the graph contains a cycle.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a"
# (red in the above image).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
# 
# 
# 
# Constraints:
# 
# 
# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        incoming, graph = [0] * n, defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            incoming[v] += 1

        stack = [u for u in range(n) if incoming[u] == 0]
        cnts = [[0] * 26 for _ in range(n)]

        while stack:
            u = stack.pop()
            cnts[u][ord(colors[u]) - ord('a')] += 1

            for v in graph[u]:
                cnts[v] = list(map(max, cnts[v], cnts[u]))
                incoming[v] -= 1
                if incoming[v] == 0:
                    stack.append(v)

        return -1 if sum(incoming) > 0 else max([max(node) for node in cnts])
        
        
# @lc code=end

