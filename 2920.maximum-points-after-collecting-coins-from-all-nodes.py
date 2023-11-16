#
# @lc app=leetcode id=2920 lang=python3
#
# [2920] Maximum Points After Collecting Coins From All Nodes
#

# @lc code=start
from functools import cache

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:

        # floor(coin / 2) is same as the bit shift to right.
        # We use v to represent the number of bit shifts.
        # Noticed that coins[i] <= 1000,
        # so after 14 bit shift,
        # no coin will be left.

        n = len(edges) + 1
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        @cache
        def dp(i, pre, v):
            if v > 13: return 0
            c = coins[i] >> v
            op1 = c - k + sum(dp(j, i, v) for j in graph[i] if j != pre)
            if c >= k + k: return op1

            op2 = (c >> 1) + sum(dp(j, i, v + 1) for j in graph[i] if j != pre)
            return max(op1, op2)

        return dp(0, -1, 0)
        
# @lc code=end

