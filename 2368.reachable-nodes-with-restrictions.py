#
# @lc app=leetcode id=2368 lang=python3
#
# [2368] Reachable Nodes With Restrictions
#

# @lc code=start
from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        def dfs(node: int) -> None:
            if node not in seen:
                seen.add(node)
                for nei in g[node]:
                    dfs(nei)

        seen = set(restricted)
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        dfs(0)
        return len(seen) - len(restricted)
        
# @lc code=end

