#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
#
# algorithms
# Hard (52.15%)
# Likes:    180
# Dislikes: 27
# Total Accepted:    3.8K
# Total Submissions: 7.2K
# Testcase Example:  '5\n[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]'
#
# Given a weighted undirected connected graph with n vertices numbered from 0
# to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a
# bidirectional and weighted edge between nodes ai and bi. A minimum spanning
# tree (MST) is a subset of the graph's edges that connects all vertices
# without cycles and with the minimum possible total edge weight.
# 
# Find all the critical and pseudo-critical edges in the given graph's minimum
# spanning tree (MST). An MST edge whose deletion from the graph would cause
# the MST weight to increase is called a critical edge. On the other hand, a
# pseudo-critical edge is that which can appear in some MSTs but not all.
# 
# Note that you can return the indices of the edges in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 5, edges =
# [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:
# 
# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are
# critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are
# considered pseudo-critical edges. We add them to the second list of the
# output.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight,
# choosing any 3 edges from the given 4 will yield an MST. Therefore all 4
# edges are pseudo-critical.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= ai < bi < n
# 1 <= weighti <= 1000
# All pairs (ai, bi) are distinct.
# 
# 
#

# @lc code=start
class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # The Kruskal’s algorithm finds the minimum cost spanning tree using a greedy approach: it first sorts all edges, which takes O(ELogE) time. After sorting, it iterates through all edges and apply Union-Find algorithm.
        # The Union-Find by Rank and Path Compression takes O(alpha(V) * E), where alpha(V) is the inverse of the Ackermann function and can be considered constant.
        # Time  complexity: O(ElogE + E^2 + E^2)
        # Space complexity: O(N)
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        def find_mst_not_use_this_edge(not_use):
            dsu = DSU(n)
            res = 0
            for i, (u, v, w, _) in enumerate(edges):
                if i == not_use:
                    continue
                if dsu.union(u, v):
                    res += w
            return res if all(dsu.find(i) == dsu.find(0) for i in range(n)) else float("inf")

        def find_mst_need_use_this_edge(need_use):
            dsu = DSU(n)
            res = edges[need_use][2]
            dsu.union(edges[need_use][0], edges[need_use][1])

            for i, (u, v, w, _) in enumerate(edges):
                if i == need_use:
                    continue
                if dsu.union(u, v):
                    res += w
                
            return res if all(dsu.find(i) == dsu.find(0) for i in range(n)) else float("inf")

        base = find_mst_not_use_this_edge(-1)
        cri, p_cri = [], []

        for i in range(len(edges)):
            v = find_mst_not_use_this_edge(i)
            if v > base:
                cri.append(edges[i][3])
            else:
                v = find_mst_need_use_this_edge(i)
                if v == base:
                    p_cri.append(edges[i][3])

        return [cri, p_cri]
        
# @lc code=end

