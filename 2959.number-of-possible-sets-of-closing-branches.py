#
# @lc app=leetcode id=2959 lang=python3
#
# [2959] Number of Possible Sets of Closing Branches
#

# @lc code=start
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:

        ans = 0
        for i in range(1 << n):
            g = [[float('inf')] * n for _ in range(n)]

            for u, v, w in roads:
                if ((i >> u) & 1) and ((i >> v) & 1):
                    g[u][v] = min(g[u][v], w)
                    g[v][u] = min(g[v][u], w)

            for j in range(n):
                g[j][j] = 0

            for p in range(n):
                for q in range(n):
                    for k in range(n):
                        g[q][k] = min(g[q][k], g[q][p] + g[p][k])


            ok = 1
            for j in range(n):
                for k in range(n):
                    if ((i >> j) & 1) and ((i >> k) & 1):
                        ok &= 1 if g[j][k] <= maxDistance else 0

            ans += ok

        return ans
        
# @lc code=end

