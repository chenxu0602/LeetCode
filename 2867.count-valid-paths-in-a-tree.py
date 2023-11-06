#
# @lc app=leetcode id=2867 lang=python3
#
# [2867] Count Valid Paths in a Tree
#

# @lc code=start
MX = 100001
lpf = [0] * MX
for i in range(2, MX):
    if lpf[i] == 0:
        for j in range(i, MX, i):
            lpf[j] = i

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
        self.siz = [1] * N

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
        return True
        
    def size(self, x):
        return self.siz[self.find(x)]

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n + 1)
        for u, v in edges:
            if lpf[u] != u and lpf[v] != v:
                dsu.union(u, v)

        count = [1] * (n + 1)   
        ans = 0
        for u, v in edges:
            if (lpf[u] == u) ^ (lpf[v] == v):
                if lpf[u] != u:
                    u, v = v, u

                ans += count[u] * dsu.size(v)
                count[u] += dsu.size(v)

        return ans
