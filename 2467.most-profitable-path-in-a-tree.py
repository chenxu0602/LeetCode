#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        # d0 is the distance from 0 to node i
        # db is the distance from i to node bob
        # if node i is not ancestor of bob, we define db >= n

        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [0] * n

        def dfs(i, d0):
            seen[i] = 1
            res = float("-inf")
            db = 0 if i == bob else n

            for j in graph[i]:
                if seen[j]: continue
                cur, kk = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)

            if res == float("-inf"):
                res = 0

            if d0 == db: res += amount[i] // 2
            if d0 < db: res += amount[i]

            return res, db + 1

        return dfs(0, 0)[0]
        
# @lc code=end

