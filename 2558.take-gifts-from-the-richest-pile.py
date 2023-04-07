#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        nums = [-num for num in gifts]
        heapq.heapify(nums)

        while k:
            tmp = math.isqrt(-heapq.heappop(nums))
            heapq.heappush(nums, -tmp)
            k -= 1

        return -sum(nums)
        
# @lc code=end

