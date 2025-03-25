#
# @lc app=leetcode id=3311 lang=python3
#
# [3311] Construct 2D Grid Matching Graph Layout
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u] += v,
            adj[v] += u,

        deg = [len(row) for row in adj]
        root = deg.index(min(deg))
        path = [root]
        seen = [0] * n
        seen[root ] = 1

        for node in path:
            if len(path) >= 2 and deg[path[-1]] == deg[root]:
                break

            adj[node].sort(key=deg.__getitem__)
            for nei in adj[node]:
                if not seen[nei] and deg[nei] <= deg[root] + 1:
                    path += nei,
                    seen[nei] = 1
                    break

        C = len(path)
        R = n // C

        ans = [[0] * C for _ in range(R)]
        ans[0] = path
        for r in range(1, R):
            for c in range(C):
                for nei in adj[ans[r - 1][c]]:
                    if not seen[nei]:
                        ans[r][c] = nei
                        seen[nei] = 1
                        break

        return ans



        
# @lc code=end

