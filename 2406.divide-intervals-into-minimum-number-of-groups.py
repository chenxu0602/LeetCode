#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heapq.heappop(pq)
            heapq.heappush(pq, right)
        return len(pq)
        """

        A = []
        for a, b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])

        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res
        
# @lc code=end

