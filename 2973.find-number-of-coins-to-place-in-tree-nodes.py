#
# @lc app=leetcode id=2973 lang=python3
#
# [2973] Find Number of Coins to Place in Tree Nodes
#

# @lc code=start
from itertools import chain, combinations
from collections import defaultdict
from math import prod

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        coin = [0] * len(cost)

        def dfs(v, p):
            subtree = [cost[v]] + list(chain.from_iterable(dfs(u, v) for u in g[v] if u != p))
            candidates = sorted(subtree)[:3] + sorted(subtree)[3:][-3:]
            coin[v] = max(0, max(map(prod, combinations(candidates, 3)), default=1))
            return candidates

        dfs(0, 0)
        return coin

        
# @lc code=end

