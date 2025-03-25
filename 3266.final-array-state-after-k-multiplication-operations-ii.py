#
# @lc app=leetcode id=3266 lang=python3
#
# [3266] Final Array State After K Multiplication Operations II
#

# @lc code=start
from heapq import heapify, heappush, heappop, heappushpop

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        if multiplier == 1: return nums

        MOD = 10**9 + 7

        n = len(nums)
        unseen, ans = set(range(n)), [0] * n

        heapify(heap := list(zip(nums, range(len(nums)))))

        while k > 0 and unseen:
            num, idx = heap[0]
            heappushpop(heap, (num * multiplier, idx))
            k -= 1
            unseen.discard(idx)

        # The order will not change from now on.
        for i in range(n):
            num, idx = heappop(heap)
            ans[idx] = (num * pow(multiplier, k // n + (i < k % n), MOD)) % MOD

        return ans


        
# @lc code=end

