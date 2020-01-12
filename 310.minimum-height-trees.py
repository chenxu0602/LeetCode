#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (30.18%)
# Likes:    982
# Dislikes: 60
# Total Accepted:    65.4K
# Total Submissions: 216.4K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
# Example 1 :
# 
# 
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3 
# 
# Output: [1]
# 
# 
# Example 2 :
# 
# 
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5 
# 
# Output: [3, 4]
# 
# Note:
# 
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
#
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        """
        if not edges or n == 1:
            return [0]

        neighbors = defaultdict(dict)

        for x, y in edges:
            neighbors[x][y] = 1
            neighbors[y][x] = 1

        while len(neighbors) > 2:
            leaves = [node for node in neighbors if len(neighbors[node]) == 1]

            for node in leaves:
                other = list(neighbors[node].keys())[0]
                del neighbors[node]
                del neighbors[other][node]

        return list(neighbors.keys())
        """

        """
        if not edges or n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
        """

        if not edges or n == 1:
            return [0]

        neighbors = [[0] * n for _ in range(n)]
        for x, y in edges:
            neighbors[x][y] = 1
            neighbors[y][x] = 1

        leaves = [i for i in range(n) if sum(neighbors[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for node in leaves:
                other = neighbors[node].index(1)
                neighbors[node][other] = 0
                neighbors[other][node] = 0
                if sum(neighbors[other]) == 1:
                    newLeaves.append(other)
            leaves = newLeaves

        return leaves
        

            




        


        

