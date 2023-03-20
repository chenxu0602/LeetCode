#
# @lc app=leetcode id=2497 lang=python3
#
# [2497] Maximum Star Sum of a Graph
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        graph = defaultdict(set)
        for u, v in edges:
            if vals[u] > 0: graph[v].add(u)
            if vals[v] > 0: graph[u].add(v)

        return max(v + sum(sorted([vals[j] for j in graph[i]], reverse=True)[0:k]) for i, v in enumerate(vals))
        
# @lc code=end

