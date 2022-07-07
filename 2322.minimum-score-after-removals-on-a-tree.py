#
# @lc app=leetcode id=2322 lang=python3
#
# [2322] Minimum Score After Removals on a Tree
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:

        n, m = map(len, (nums, edges))

        graph = defaultdict(list)
        children = defaultdict(set)

        xors = nums[:]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        V = 0
        seen = set()
        queue = deque()
        for i in range(n):
            V ^= nums[i]
            if degree[i] == 1:
                queue.append(i)
                seen.add(i)

        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if nxt not in seen: # 'nxt is not in seen' means that node 'nxt' is the parent of node 'cur'.
                    children[nxt].add(cur)
                    children[nxt] |= children[cur]
                    xors[nxt] ^= xors[cur]

                degree[nxt] -= 1
                if degree[nxt] == 1:
                    seen.add(nxt)
                    queue.append(nxt)

        ans = float("inf")
        for i in range(m - 1):
            for j in range(i + 1, m):
                u, v = edges[i]
                if v in children[u]:
                    u, v = v, u

                x, y = edges[j]
                if y in children[x]:
                    x, y = y, x

                if x in children[u]:
                    cur = [xors[x], xors[u] ^ xors[x], V ^ xors[u]]
                elif u in children[x]:
                    cur = [xors[u], xors[x] ^ xors[u], V ^ xors[x]]
                else:
                    cur = [xors[u], xors[x], V ^ xors[u] ^ xors[x]]

                ans = min(ans, max(cur) - min(cur))

        return ans
        

        
# @lc code=end

