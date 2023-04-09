#
# @lc app=leetcode id=2581 lang=python3
#
# [2581] Count Number of Possible Root Nodes
#

# @lc code=start
from collections import defaultdict, Counter
from functools import lru_cache

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:

        adj, g = defaultdict(set), Counter(map(tuple, guesses))
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        @lru_cache(None)
        def t(cur, pre):
            return g[pre, cur] + sum(t(kid, cur) for kid in adj[cur] - {pre})

        return sum(t(i, -1) >= k for i in adj)
        
# @lc code=end

