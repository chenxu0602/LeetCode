#
# @lc app=leetcode id=2493 lang=python3
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        uf = {}

        def find(x):
            if not x in uf:
                uf[x] = x

            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]
        
        def union(x, y):
            xr, yr = map(find, (x, y))
            uf[xr] = yr 

        def bfs(node):
            queue = deque([(node, 1)])
            seen = {node: 1}
            level = 1

            while queue:
                cur, lvl = queue.popleft()
                for nei in graph[cur]:
                    if not nei in seen:
                        seen[nei] = lvl + 1
                        queue.append((nei, lvl + 1))
                    # check if there is a odd number edges cycle
                    elif seen[nei] == lvl:
                        return -1

            return lvl

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            union(u, v)

        # Store the largest group in each connected component
        maxGroup = defaultdict(int)
        # Start a BFS on each node, and update the maxGroup for each connected component
        for i in range(1, n + 1):
            groups = bfs(i)
            # There is a odd number edges cycle, so return -1
            if groups == -1: return -1

            root = find(i)
            maxGroup[root] = max(maxGroup[root], groups)

        return sum(maxGroup.values())

            


        
# @lc code=end

