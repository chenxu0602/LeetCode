#
# @lc app=leetcode id=3275 lang=python3
#
# [3275] K-th Nearest Obstacle Queries
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:

        max_heap, ans, n = [], [], len(queries)

        for i in range(n):
            x, y = queries[i][0], queries[i][1]
            dist = abs(x) + abs(y)
            heappush(max_heap, -dist)

            if len(max_heap) > k:
                heappop(max_heap)
            
            if len(max_heap) == k:
                ans += -max_heap[0],
            else:
                ans += -1,

        return ans

        
# @lc code=end

