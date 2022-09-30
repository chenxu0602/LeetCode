#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
#

# @lc code=start
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n
        self.siz = [1] * n

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
        self.siz[xr] += self.siz[yr]


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        n = len(vals)
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        valNodes = defaultdict(list)
        for i in range(n):
            valNodes[vals[i]].append(i)

        dsu = DSU(n)
        res = n

        for val in sorted(valNodes):
            for curr in valNodes[val]:
                for adj in adjList[curr]:
                    if vals[adj] <= vals[curr]:
                        dsu.union(curr, adj)

            group = defaultdict(int)
            for curr in valNodes[val]:
                group[dsu.find(curr)] += 1

            for _, cnt in group.items():
                if cnt >= 2:
                    res += cnt * (cnt - 1) // 2

        return res
        
# @lc code=end

