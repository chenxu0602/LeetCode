#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (40.28%)
# Likes:    754
# Dislikes: 24
# Total Accepted:    101.9K
# Total Submissions: 250.7K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
# 
# Example 1:
# 
# 
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# 
# Example 2:
# 
# 
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
# 
#

# @lc code=start
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))

        """
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

#            if parent[x] != x:
#                parent[x] = find(parent[x])
#            return parent[x]


        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y

        return len(edges) == n - 1 and all(map(union, edges))
        """

        """
        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,

        def visit(v):
            list(map(visit, neighbors.pop(v, [])))

        visit(0)
        return not neighbors
        """

        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,

        queue = deque([0])
        while queue:
            queue.extend(neighbors.pop(queue.popleft(), []))

        return not neighbors

        
# @lc code=end

