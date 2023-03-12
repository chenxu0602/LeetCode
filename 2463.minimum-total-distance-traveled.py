#
# @lc app=leetcode id=2463 lang=python3
#
# [2463] Minimum Total Distance Traveled
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()

        nr, nf = len(robot), len(factory)

        # dp(i,j,k) means the cost that,
        # to fix robot[i] and its following roberts
        # with factory[j] already fix k robert.
        @lru_cache(None)
        def dp(i, j, k):
            if i == nr: return 0
            if j == nf: return float("inf")

            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0]) if factory[j][1] > k else float("inf")

            return min(res1, res2)

        return dp(0, 0, 0)
        
# @lc code=end

