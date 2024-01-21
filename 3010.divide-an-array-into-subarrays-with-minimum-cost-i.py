#
# @lc app=leetcode id=3010 lang=python3
#
# [3010] Divide an Array Into Subarrays With Minimum Cost I
#

# @lc code=start
from heapq import heappush, heappop, heappushpop

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        # n = len(nums)
        # s = nums[0]
        # nums[1:n] = sorted(nums[1:n])
        # s += nums[1] + nums[2]
        # return s


        heap = []
        heappush(heap, -nums[1])
        heappush(heap, -nums[2])

        for num in nums[3:]:
            heappushpop(heap, -num)

        return nums[0] - heap[0] - heap[1]
        
# @lc code=end

