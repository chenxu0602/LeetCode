#
# @lc app=leetcode id=3244 lang=python3
#
# [3244] Shortest Distance After Road Addition Queries II
#

# @lc code=start
from sortedcontainers import SortedSet

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        # sorted_set = SortedSet()
        # for i in range(n):
        #     sorted_set.add(i)

        # res = []
        # for u, v in queries:
        #     ini = sorted_set.bisect_right(u)
        #     while sorted_set[ini] < v:
        #         sorted_set.pop(ini)
        #     res += len(sorted_set) - 1,

        # return res

        next = [i + 1 for i in range(n)]
        next[n - 1] = -1

        dist = n - 1
        res = []

        for u, v in queries:
            if next[u] == -1 or v < next[u]:
                res += dist,
            else:
                curr = next[u]
                while curr != v:
                    next[curr], curr = -1, next[curr]
                    dist -= 1

                next[u] = v
                res += dist,

        return res



        
# @lc code=end

