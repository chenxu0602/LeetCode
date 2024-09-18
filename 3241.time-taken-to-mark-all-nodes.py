#
# @lc app=leetcode id=3241 lang=python3
#
# [3241] Time Taken to Mark All Nodes
#

# @lc code=start
from collections import defaultdict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:

        n = len(edges) + 1
        dp = [[0, 0] for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u] += v,
            graph[v] += u,

        def dfs1(node, par):
            for nxt in graph[node]:
                if nxt == par: continue
                add = 2 if nxt % 2 == 0 else 1
                v = dfs1(nxt, node)
                if v + add >= dp[node][0]:
                    dp[node] = [v + add, dp[node][0]]
                elif v + add > dp[node][1]:
                    dp[node][1] = v + add

            return dp[node][0]

        def dfs2(node, par):
            if par != -1:
                par_to_node_add = 2 if node % 2 == 0 else 1
                node_to_par_add = 2 if par % 2 == 0 else 1
                if dp[par][0] == dp[node][0] + par_to_node_add:
                    par_max_time_taken = dp[par][1] + node_to_par_add
                else:
                    par_max_time_taken = dp[par][0] + node_to_par_add

                if par_max_time_taken >= dp[node][0]:
                    dp[node] = [par_max_time_taken, dp[node][0]]
                elif par_max_time_taken > dp[node][1]:
                    dp[node][1] = par_max_time_taken

            for nxt in graph[node]:
                if nxt == par: continue
                dfs2(nxt, node)


        dfs1(0, -1)
        dfs2(0, -1)
        return [x[0] for x in dp]

        
# @lc code=end

