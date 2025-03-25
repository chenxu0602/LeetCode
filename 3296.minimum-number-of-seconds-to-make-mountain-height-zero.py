#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#

# @lc code=start
from heapq import heapify, heappush, heappop

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        heap = [(t, t, 1) for t in workerTimes]
        heapify(heap)

        while mountainHeight > 1:     # In the end we return top of the heap
            tot, init, freq = heappop(heap)
            heappush(heap, (tot + init * (freq + 1), init, freq + 1))
            mountainHeight -= 1

        return heappop(heap)[0]

        
# @lc code=end

