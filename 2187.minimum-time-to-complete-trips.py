#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        # O(nlog(min(time) * totalTrips))

        lo, hi = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if not f(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo
        
# @lc code=end

