#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Time  complexity: O(edges)
        # Space complexity: O(edges)

        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = [0] * n

        res = 0
        for i in range(n):
            if seen[i]: continue
            bfs = [i]
            seen[i] = 1
            for j in bfs:
                for k in graph[j]:
                    if seen[k] == 0:
                        bfs.append(k) 
                        seen[k] = 1

            if all(len(graph[j]) == len(bfs) - 1 for j in bfs):
                res += 1

        return res
        
# @lc code=end

