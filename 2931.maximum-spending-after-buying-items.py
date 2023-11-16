#
# @lc app=leetcode id=2931 lang=python3
#
# [2931] Maximum Spending After Buying Items
#

# @lc code=start
import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:

        # return sum(d * a for d, a in enumerate(sorted(a for r in values for a in r), 1))

        # Time  complexity: O(mnlogm)
        # Space complexity: O(m)
        m, n = map(len, (values, values[0]))
        heap = [(values[i].pop(), i) for i in range(m)]
        heapq.heapify(heap)
        res = 0
        for d in range(1, m * n + 1):
            v, i = heapq.heappop(heap)
            res += v * d
            if values[i]:
                heapq.heappush(heap, (values[i].pop(), i))
        return res
        
# @lc code=end

