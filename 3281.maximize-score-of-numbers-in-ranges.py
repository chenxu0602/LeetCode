#
# @lc app=leetcode id=3281 lang=python3
#
# [3281] Maximize Score of Numbers in Ranges
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        """
        start.sort()
        n = len(start)
        l = 0
        r = start[-1] - start[0] + d + 1

        def isPossible(score):
            pre = start[0]
            for i in range(1, n):
                if start[i] + d - pre < score:
                    return False
                pre = max(start[i], pre + score)
            return True

        while l < r:
            m = l + (r - l) // 2
            if isPossible(m):
                l = m + 1
            else:
                r = m

        return l - 1
        """

        """
        start.sort()

        def fn(mid):
            x = float('-inf')
            for s in start:
                x += mid
                if x > s + d: return False
                x = max(x, s)
            return True

        lo, hi = 0, 2 * 10**9
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if fn(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
        """

        def fail_check(mid):
            nonlocal start
            prev = start[0]

            for s in start[1:]:
                prev += mid
                if prev > s + d:
                    return True
                if s > prev:
                    prev = s

            return False


        start.sort()
        max_ = start[-1] + d + 1

        return bisect_left(range(max_), True, key=fail_check) - 1


        
# @lc code=end

