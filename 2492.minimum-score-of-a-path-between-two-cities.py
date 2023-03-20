#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        res = float("inf")
        seen = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, scr in graph[node].items():
                if adj not in seen:
                    queue.append(adj)
                    seen.add(adj)
                res = min(res, scr)

        return res
        
# @lc code=end

