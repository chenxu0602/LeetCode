#
# @lc app=leetcode id=2386 lang=python3
#
# [2386] Find the K-Sum of an Array
#

# @lc code=start
import heapq

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:

        # Time  complexity: O(nlogn + klogk)
        # Space complexity: O(n + k)

        m = sum(x for x in nums if x > 0)
        pq = [(-m, 0)]
        vals = sorted(abs(x) for x in nums)

        for _ in range(k):
            x, i = heapq.heappop(pq)
            if i < len(vals):
                heapq.heappush(pq, (x + vals[i], i + 1))
                if i:
                    heapq.heappush(pq, (x - vals[i - 1] + vals[i], i + 1))

        return -x
        
# @lc code=end

