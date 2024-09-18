#
# @lc app=leetcode id=3249 lang=python3
#
# [3249] Count the Number of Good Nodes
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:

        graph, ans = defaultdict(list), 0

        for u, v in edges:
            graph[u] += v,
            graph[v] += u,

        def dfs(node, par):
            nonlocal ans
            subtree_sizes = []

            for child in graph[node]:
                if child != par:
                    subtree_size = dfs(child, node)
                    subtree_sizes += subtree_size,

            if len(set(subtree_sizes)) <= 1:
                ans += 1

            return sum(subtree_sizes) + 1   


        dfs(0, -1)
        return ans

        
# @lc code=end

