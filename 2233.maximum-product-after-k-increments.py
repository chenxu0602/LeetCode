#
# @lc app=leetcode id=2233 lang=python3
#
# [2233] Maximum Product After K Increments
#

# @lc code=start
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:

        # Product of the array will be maximum when the smallest number in the array is maximum.
        # We use priority queue to find the smallest element in every iteration and increase it by 1.
        MOD = 10**9 + 7
        pq = []

        for i in range(len(nums)):
            heapq.heappush(pq, nums[i])

        while k > 0:
            x = heapq.heappop(pq)
            x += 1
            heapq.heappush(pq, x)
            k -= 1

        ans = 1
        while pq:
            x = heapq.heappop(pq)
            ans = (ans * x) % MOD

        return ans
        
# @lc code=end

