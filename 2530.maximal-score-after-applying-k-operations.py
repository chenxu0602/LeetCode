#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        pq = [-x for x in nums]
        heapq.heapify(pq)
        ans = 0
        for _ in range(k):
            ans -= pq[0]
            heapq.heapreplace(pq, pq[0] // 3)

        return ans
        
# @lc code=end

