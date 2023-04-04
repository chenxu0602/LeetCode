#
# @lc app=leetcode id=2538 lang=python3
#
# [2538] Difference Between Maximum and Minimum Price Sum
#

# @lc code=start
from collections import defaultdict
from functools import lru_cache

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:

        """
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        @lru_cache(None)
        def dfs(cur, pre):
            return price[cur] + max([dfs(nxt, cur) for nxt in adj[cur] - {pre}] + [0])
        
        return max(dfs(i, -1) - price[i] for i in range(n))
        """
# @lc code=end

