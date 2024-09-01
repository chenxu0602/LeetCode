#
# @lc app=leetcode id=3049 lang=python3
#
# [3049] Earliest Second to Mark Indices II
#

# @lc code=start
from bisect import bisect_left
from heapq import heappush, heappop

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:

        change = {}
        for i, mark in enumerate(changeIndices, 1):
            if nums[mark - 1] > 1 and mark - 1 not in change:
                change[mark - 1] = i

        change = sorted((v, k) for k, v in change.items())

        def check(t):
            size = 1
            h = []
            j = bisect_left(change, t, key=lambda x: x[0]) - 1
            for i in range(t - 1, 0, -1):
                if j >= 0 and i == change[j][0]:
                    k = change[j][1]
                    heappush(h, (nums[k], k))
                    j -= 1
                    while len(h) > size:
                        heappop(h)
                        size += 1
                else:
                    size += 1

            return t >= sum(nums) - sum(v for v, _ in h) + len(h) + len(nums)


        p = bisect_left(range(1, len(changeIndices) + 1), 1, key=check) + 1
        return p if 1 <= p <= len(changeIndices) else -1

        
# @lc code=end

