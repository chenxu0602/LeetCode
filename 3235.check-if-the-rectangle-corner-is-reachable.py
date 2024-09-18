#
# @lc app=leetcode id=3235 lang=python3
#
# [3235] Check if the Rectangle Corner Is Reachable
#

# @lc code=start

class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

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


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:

        n = len(circles)

        dsu = DSU(n + 2)

        for i in range(n):
            x1, y1, r1 = circles[i]
            for j in range(i + 1, n):
                x2, y2, r2 = circles[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if d <= (r1 + r2) ** 2:
                    dsu.union(i, j)

        for i in range(n):
            x, y, r = circles[i]
            # if x - r >= xCorner and y - r >= yCorner: continue
            if x - r <= 0 or y + r >= yCorner:
                dsu.union(n, i)
            if x + r >= xCorner or y - r <= 0:
                dsu.union(n + 1, i)

        return dsu.find(n) != dsu.find(n + 1)


        
# @lc code=end

