#
# @lc app=leetcode id=2532 lang=python3
#
# [2532] Time to Cross a Bridge
#

# @lc code=start
import heapq

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:

        ans = free = 0
        l, ll = [], []
        r, rr = [], []

        for i, (x, _, y, _) in enumerate(time):
            heapq.heappush(ll, (-x-y, -i))

        while n or r or rr:
            if not rr and (not r or r[0][0] > free) and (not n or not ll and (not l or l[0][0] > free)):
                cand = float("inf")
                if n and l: cand = min(cand, l[0][0])
                if r: cand = min(cand, r[0][0])
                free = cand

            while r and r[0][0] <= free:
                _, i = heapq.heappop(r)
                heapq.heappush(rr, (-time[i][0] - time[i][2], -i))

            while l and l[0][0] <= free:
                _, i = heapq.heappop(l)
                heapq.heappush(ll, (-time[i][0] - time[i][2], -i))

            if rr:
                _, i = heapq.heappop(rr)
                free += time[-i][2]
                if n: heapq.heappush(l, (free + time[-i][3], -i))
                else: ans = max(ans, free)
            else:
                _, i = heapq.heappop(ll)
                free += time[-i][0]
                heapq.heappush(r, (free + time[-i][1], -i))
                n -= 1

        return ans
        
# @lc code=end

