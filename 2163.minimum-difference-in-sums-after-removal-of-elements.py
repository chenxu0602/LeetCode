#
# @lc app=leetcode id=2163 lang=python3
#
# [2163] Minimum Difference in Sums After Removal of Elements
#

# @lc code=start
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums) // 3

        pre_min, cur_min = [sum(nums[:n])], sum(nums[:n])
        pre_heap = [-x for x in nums[:n]]
        heapq.heapify(pre_heap)

        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(pre_heap)
            cur_min -= cur_pop
            cur_min += min(cur_pop, nums[i])
            pre_min.append(cur_min)
            heapq.heappush(pre_heap, -min(cur_pop, nums[i]))

        suf_max, cur_max = [sum(nums[2*n:])], sum(nums[2*n:])
        suf_heap = [x for x in nums[2*n:]]
        heapq.heapify(suf_heap)

        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(suf_heap)
            cur_max -= cur_pop
            cur_max += max(cur_pop, nums[i])
            suf_max.append(cur_max)
            heapq.heappush(suf_heap, max(cur_pop, nums[i]))

        suf_max = suf_max[::-1]

        ans = float("inf")
        for a, b in zip(pre_min, suf_max):
            ans = min(ans, a - b)
        return ans
        
# @lc code=end

