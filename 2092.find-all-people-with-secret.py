#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
from collections import defaultdict
import itertools

class Union:
    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        return True

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        """
        can = {0, firstPerson}
        for _, grp in itertools.groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            stack = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)

                if x in can:
                    stack.add(x)
                if y in can:
                    stack.add(y)

            stack = list(stack)
            while stack:
                x = stack.pop()
                for y in graph[x]:
                    if y not in can:
                        can.add(y)
                        stack.append(y)

        return can
        """

        uf = Union(n)
        uf.union(0, firstPerson)
        for _, grp in itertools.groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            seen = set()
            for x, y, _ in grp:
                seen.add(x)
                seen.add(y)
                uf.union(x, y)

            for x in seen:
                if uf.find(x) != uf.find(0):
                    uf.par[x] = x

        return [x for x in range(n) if uf.find(x) == uf.find(0)]
        
# @lc code=end

