#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = []
        for x in nums:
            heapq.heappush(minHeap, int(x))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return str(minHeap[0])
        
# @lc code=end

