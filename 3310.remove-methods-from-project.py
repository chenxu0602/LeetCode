#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        visited = [False] * n

        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u] += v,

        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        dfs(k)

        default_ans = list(range(n))
        ans = []
        for node in range(n):
            if not visited[node]:
                ans += node,
                for nei in adj[node]:
                    if visited[nei]:
                        return default_ans

        return ans
        
# @lc code=end

