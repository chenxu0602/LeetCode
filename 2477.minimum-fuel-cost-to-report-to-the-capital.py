#
# @lc app=leetcode id=2477 lang=python3
#
# [2477] Minimum Fuel Cost to Report to the Capital
#

# @lc code=start
from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0

        def dfs(u, prev, people = 1):
            for v in graph[u]:
                if v == prev: continue
                people += dfs(v, u)

            self.ans += (int(math.ceil(people / seats)) if u else 0)
            return people

        dfs(0, -1)
        return self.ans

        
# @lc code=end

