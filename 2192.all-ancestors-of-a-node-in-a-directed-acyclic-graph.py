#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # direct_child = defaultdict(list)
        # ans = [[] for _ in range(n)]
        # for x, y in edges:
        #     direct_child[x].append(y)

        # def dfs(x, curr):
        #     for ch in direct_child[curr]:
        #         if ans[ch] and ans[ch][-1] == x: continue
        #         ans[ch].append(x)
        #         dfs(x, ch)

        # for i in range(n): dfs(i, i)
        # return ans

        ans = [set() for _ in range(n)]
        graph = defaultdict(list)
        inDegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            inDegree[v] += 1

        q = deque([i for i, d in enumerate(inDegree) if d == 0])

        while q:
            u = q.popleft()
            for v in graph[u]:
                ans[v].add(u)
                ans[v].update(ans[u])
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        return [sorted(i) for i in ans]
        
        
# @lc code=end

