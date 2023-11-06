#
# @lc app=leetcode id=2858 lang=python3
#
# [2858] Minimum Edge Reversals So Every Node Is Reachable
#

# @lc code=start
from collections import defaultdict, deque
from functools import lru_cache

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:

        # G[i][j] is the cost to go from i to j.
        # For edge [i, j],
        # we have G[i][j] = 0, G[j][i] = 1.
        # In each call of dfs(i, j),
        # i is the parent, j is the current node,
        # and we return the cost from j to all other nodes in this direction.
        # We recursively accumulate dfs(j, k) + G[j][k],
        # where k is the children of j.
        # and then return the sum.
        # Finally we return dfs(-1, i) for each node i as the root.
        # Time  complexity: O(n), worst O(n^2)
        # Space complexity: O(n)
        # graph = defaultdict(lambda: defaultdict(int))
        # for u, v in edges:
        #     graph[u][v], graph[v][u] = 0, 1

        # @lru_cache(None)        
        # def dp(i, j):
        #     return sum(dp(j, k) + graph[j][k] for k in graph[j] if k != i)

        # return [dp(-1, i) for i in range(n)]



        # We build an adjacency graph, in which the direction of each edge is indicated by including either 1 (not reversed) or -1 (reversed).

        # We intialize: (a) ans to track the net difference of reversed and not-reversed edges to each node as we BFS-traverse the tree with root 0, (b) zeroCnt to track the total the net difference of reversed and not-reversed edges in the tree, and (c)'queue' for BFS.

        # Finally, we use these net differences to compute ans0 = (n-1-zeroCnt)//2 , which then allows us to compute and return the desired list. (The algebraic justification for these computations is left to the interested reader.)
        graph, ans, zero_cnt = defaultdict(list), defaultdict(int), 0

        for u, v in edges:
            graph[u] += (v, 1),
            graph[v] += (u, -1),

        queue = deque([(0, 0)])
        while queue:
            parent, parent_cnt = queue.pop()
            ans[parent] = parent_cnt

            for child, cnt in graph[parent]:
                if child in ans: continue
                zero_cnt += cnt
                queue += (child, cnt + parent_cnt),

        ans0 = (n - 1 - zero_cnt) // 2
        return [ans[i] + ans0 for i in range(n)]
        
# @lc code=end

