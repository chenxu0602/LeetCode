#
# @lc app=leetcode id=1579 lang=python3
#
# [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
#
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
#
# algorithms
# Hard (45.56%)
# Likes:    252
# Dislikes: 3
# Total Accepted:    5.7K
# Total Submissions: 12.5K
# Testcase Example:  '4\n[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]'
#
# Alice and Bob have an undirected graph of n nodes and 3 types of edges:
# 
# 
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# 
# 
# Given an array edges where edges[i] = [typei, ui, vi] represents a
# bidirectional edge of type typei between nodes ui and vi, find the maximum
# number of edges you can remove so that after removing the edges, the graph
# can still be fully traversed by both Alice and Bob. The graph is fully
# traversed by Alice and Bob if starting from any node, they can reach all
# other nodes.
# 
# Return the maximum number of edges you can remove, or return -1 if it's
# impossible for the graph to be fully traversed by Alice and Bob.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will
# still be fully traversable by Alice and Bob. Removing any additional edge
# will not make it so. So the maximum number of edges we can remove is 2.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully
# traversable by Alice and Bob.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other
# nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the
# graph fully traversable.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# All tuples (typei, ui, vi) are distinct.
# 
# 
#

# @lc code=start
class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
        self.count = N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        self.count -= 1
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_a, uf_b = DSU(n), DSU(n)

        ans = 0
        edges.sort(reverse=True)

        for t, u, v in edges:
            u, v = u - 1, v - 1
            if t == 3:
                ans += not (uf_a.union(u, v) and uf_b.union(u, v))
            elif t == 2:
                ans += not uf_b.union(u, v)
            else:
                ans += not uf_a.union(u, v)

        return ans if uf_a.count == 1 and uf_b.count == 1 else -1
        
# @lc code=end

