#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n, res = len(costs), 0
        pairs = [(t, i) for i, t in enumerate(costs)]
        l, r = min(candidates, n // 2), max(n - candidates, n // 2)
        pq = pairs[:l] + pairs[r:]

        heapq.heapify(pq)

        for _ in range(k):
            cost, i = heapq.heappop(pq)
            if i < l:
                i, l = l, l + 1
            if i >= r:
                i, r = r - 1, r - 1
            if l <= r:
                heapq.heappush(pq, pairs[i])

            res += cost

        return res
        
# @lc code=end

