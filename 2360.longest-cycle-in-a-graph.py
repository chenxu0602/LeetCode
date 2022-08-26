#
# @lc app=leetcode id=2360 lang=python3
#
# [2360] Longest Cycle in a Graph
#

# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def dfs(node):
            nonlocal visited, edges, res
            mark = {node: 0}
            while visited[node] is False and node != -1:
                visited[node] = True
                nxt = edges[node]
                if nxt in mark:
                    cycleLen = len(mark) - mark[nxt]
                    res = max(res, cycleLen)
                else:
                    node = nxt
                    mark[nxt] = len(mark)

        n = len(edges)
        res = -1
        visited = [False] * n
        for i in range(n):
            dfs(i)
        return res
        
# @lc code=end

