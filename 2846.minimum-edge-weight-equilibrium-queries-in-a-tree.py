#
# @lc app=leetcode id=2846 lang=python3
#
# [2846] Minimum Edge Weight Equilibrium Queries in a Tree
#

# @lc code=start
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        m, C = n.bit_length() + 1, 27
        g = [[] for i in range(n)]
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))

        fa = [[0] * n for _ in range(m)]
        w = [None] * n
        d = [0] * n

        def dfs(x, f, dep):
            fa[0][x] = f
            d[x] = dep
            for (c, weight) in g[x]:
                if f == c: continue
                w[c] = w[x].copy()
                w[c][weight] += 1
                dfs(c, x, dep + 1)

        w[0] = [0] * C
        dfs(0, 0, 0)

        for i in range(1, m):
            for j in range(n):
                fa[i][j] = fa[i - 1][fa[i - 1][j]]

        def lca(x, y):
            if d[x] > d[y]: x, y = y, x
            for p in range(m):
                if (1 << p) & (d[y] - d[x]):
                    y = fa[p][y]

            for p in range(m - 1, -1, -1):
                if fa[p][x] != fa[p][y]:
                    x = fa[p][x]
                    y = fa[p][y]

            return x if x == y else fa[0][x]


        res = []
        for q in queries:
            x, y, l = q[0], q[1], lca(q[0], q[1])
            length = d[x] + d[y] - 2 * d[l]
            max_z = max([w[x][z] + w[y][z] - w[l][z] * 2 for z in range(1, C)])
            res.append(length - max_z)

        return res
        
# @lc code=end

