#
# @lc app=leetcode id=2508 lang=python3
#
# [2508] Add Edges to Make Degrees of All Nodes Even
#

# @lc code=start
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:

        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)

        odd = [i for i in range(n) if len(graph[i]) % 2]

        def f(a, b): return a not in graph[b]

        if len(odd) == 2:
            a, b = odd
            return any(f(a, i) and f(b, i) for i in range(n))

        if len(odd) == 4:
            a, b, c, d = odd
            return f(a, b) and f(c, d) or f(a, c) and f(b, d) or f(a, d) and f(c, b)

        return len(odd) == 0
        
# @lc code=end

