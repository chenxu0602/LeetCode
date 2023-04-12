#
# @lc app=leetcode id=2612 lang=python3
#
# [2612] Minimum Reverse Operations
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        remaining = [SortedList(), SortedList()]
        banned = set(banned)
        for i in range(n):
            if i != p and i not in banned:
                remaining[i & 1].add(i)

        queue = [p]
        dist = [-1] * n
        dist[p] = 0
        for node in queue:
            lo = max(node - k + 1, 0)
            lo = 2 * lo + k - 1 - node
            hi = min(node + k - 1, n - 1) - (k - 1)
            hi = 2 * hi + k - 1 - node

            for nei in list(remaining[lo % 2].irange(lo, hi)):
                queue.append(nei)
                dist[nei] = dist[node] + 1
                remaining[lo % 2].remove(nei)

        return dist
        
# @lc code=end

