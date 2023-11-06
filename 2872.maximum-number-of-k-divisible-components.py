#
# @lc app=leetcode id=2872 lang=python3
#
# [2872] Maximum Number of K-Divisible Components
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        # If a leaf's value is divisible by k, we can safely separate it from the tree, 
        # thus, increasing the number of components. If not, it will be a part of its 
        # parent's component. To account for the latter, it is sufficient to just increase 
        # the parent's value by the leaf's value.

        if n <= 1: return 1

        count = 0

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = deque(u for u, vs in graph.items() if len(vs) == 1)

        while queue:
            u = queue.popleft()

            p = next(iter(graph[u])) if graph[u] else -1
            if p >= 0: graph[p].remove(u)

            if values[u] % k == 0: 
                count += 1
            else:
                values[p] += values[u]

            if p >= 0 and len(graph[p]) == 1: 
                queue.append(p)

        return count
        
# @lc code=end

