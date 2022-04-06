#
# @lc app=leetcode id=2157 lang=python3
#
# [2157] Groups of Strings
#

# @lc code=start
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
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr

        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:

        n = len(words)
        dsu = DSU(n)
        dt = dict()

        for i, w in enumerate(words):
            x = sum(1 << ord(c) - ord('a') for c in w)
            if x in dt:
                dsu.union(i, dt[x])

            for j in range(26):
                if x & (1 << j):
                    y = x ^ (1 << j)
                    if y in dt:
                        dsu.union(i, dt[y])
                    dt[y] = i

            dt[x] = i

        for i in range(n):
            dsu.find(i)

        return [len(set(dsu.par)), max(dsu.siz)]

        
# @lc code=end

