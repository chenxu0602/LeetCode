#
# @lc app=leetcode id=2208 lang=python3
#
# [2208] Minimum Operations to Halve Array Sum
#

# @lc code=start
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        q, s, k, i = [], sum(nums), 0, 0
        for x in nums:
            heapq.heappush(q, -x)

        while s - k > s / 2:
            x = -heapq.heappop(q)
            k += x / 2
            heapq.heappush(q, -x / 2)
            i += 1

        return i
        
# @lc code=end

