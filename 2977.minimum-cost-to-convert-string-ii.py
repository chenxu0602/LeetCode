#
# @lc app=leetcode id=2977 lang=python3
#
# [2977] Minimum Cost to Convert String II
#

# @lc code=start
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        lookup = {a: {} for a in set(original)}

        def bfs(a):
            heap = [(0, a)]
            visited = set()
            while heap:
                curr_cost, b = heappop(heap)
                if b in visited:
                    continue
                visited.add(b)
                lookup[a][b] = curr_cost
                for c in graph[b]:
                    heappush(heap, (curr_cost + graph[b][c], c))


        graph = defaultdict(dict)
        for x, y, z in zip(original, changed, cost):
            if y not in graph[x]:
                graph[x][y] = z
            else:
                graph[x][y] = min(graph[x][y], z)

        for a in set(original):
            bfs(a)

        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]

            for l in set(len(s) for s in original):
                if i >= l and (s := source[i - l:i]) in lookup and (t := target[i - l:i]) in lookup[s]:
                    dp[i] = min(dp[i], dp[i - l] + lookup[s][t])

        return dp[-1] if dp[-1] < float('inf') else -1



        
# @lc code=end

