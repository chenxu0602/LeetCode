#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (52.08%)
# Likes:    407
# Dislikes: 12
# Total Accepted:    62K
# Total Submissions: 118.8K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
# 
# Example 1:
# 
# 
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# 
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4 
# 
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
# 
# Output:  1
# 
# 
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
#
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # p = list(range(n))
        # def find(v):
        #     if p[v] != v:
        #         p[v] = find(p[v])
        #     return p[v]

        # for v, w in edges:
        #     p[find(v)] = find(w)

        # return len(set(map(find, p)))

        p = list(range(n))

        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]

        for e in edges:
            v, w = map(find, e)
            p[v] = w
            n -= v != w
        return n
        

