#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (57.16%)
# Likes:    1444
# Dislikes: 228
# Total Accepted:    100.4K
# Total Submissions: 174.2K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# The given input is a graph that started as a tree with N nodes (with distinct
# values 1, 2, ..., N), with one additional edge added.  The added edge has two
# different vertices chosen from 1 to N, and was not an edge that already
# existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
# 
# Return an edge that can be removed so that the resulting graph is a tree of N
# nodes.  If there are multiple answers, return the answer that occurs last in
# the given 2D-array.  The answer edge [u, v] should be in the same format,
# with u < v.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
# ⁠ 1
# ⁠/ \
# 2 - 3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
# 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
# 
# 
# 
# 
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly
# the graph is an undirected graph. For the directed graph follow up please see
# Redundant Connection II). We apologize for any inconvenience caused.
# 
#

# @lc code=start
from collections import defaultdict

class DSU:
    def __init__(self):
        self.par = list(range(10001))
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[yr] < self.rnk[xr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS
        # For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v. If we can, then it must be the duplicate edge.
        # Time  complexity: O(N^2) where N is the number of vertices.
        # Space complexity: O(N)
        # graph = defaultdict(set)

        # def dfs(source, target):
        #     if source not in seen:
        #         seen.add(source)
        #         if source == target: return True
        #         return any(dfs(nei, target) for nei in graph[source])

        # for u, v in edges:
        #     seen = set()
        #     if u in graph and v in graph and dfs(u, v):
        #         return u, v
        #     graph[u].add(v)
        #     graph[v].add(u)


        # Union-Find
        # Time  complexity: O(N x a(N)) = O(N), where N is the number of vertices and alpha is the Inverse-Ackermann function.
        # Space complexity: O(N)
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
        
# @lc code=end

