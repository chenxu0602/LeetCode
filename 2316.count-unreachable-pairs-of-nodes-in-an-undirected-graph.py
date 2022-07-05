#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        def dfs(v):
            if visited[v]:
                return 0
            visited[v] = True
            res = 1
            for nei in graph[v]:
                res += dfs(nei)
            return res

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        components = []

        for i in range(n):
            if visited[i] is False:
                components.append(dfs(i))

        ans = n * (n - 1) // 2

        for i in components:
            ans -= i * (i - 1) // 2

        return ans
        
# @lc code=end

