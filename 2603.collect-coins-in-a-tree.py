#
# @lc app=leetcode id=2603 lang=python3
#
# [2603] Collect Coins in a Tree
#

# @lc code=start
from collections import defaultdict

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        if not edges: return 0

        n = len(edges) + 1

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [u for u in graph if len(graph[u]) == 1]
        for u in leaves:
            while len(graph[u]) == 1 and coins[u] == 0:
                v = graph[u].pop()
                del graph[u]
                graph[v].remove(u)
                u = v

        for _ in range(2):
            leaves = [u for u in graph if len(graph[u]) == 1]
            for u in leaves:
                v = graph[u].pop()
                del graph[u]
                graph[v].remove(u)
                if len(graph) < 2:
                    return 0

        return 2 * (len(graph) - 1)
        
# @lc code=end

