#
# @lc app=leetcode id=3288 lang=python3
#
# [3288] Length of the Longest Increasing Path
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:

        less    = lambda z: z[0] < max_x and z[1] < max_y
        greater = lambda z: z[0] > max_x and z[1] > max_y
        order   = lambda z: (z[0], -z[1])

        def lis(arr):
            res = []
            for _, y in arr:
                if not res or y > res[-1]: 
                    res += y,
                else:
                    res[bisect_left(res, y)] = y

            return len(res)


        max_x, max_y = coordinates[k]

        left  = lis(sorted(filter(less, coordinates), key=order))
        right = lis(sorted(filter(greater, coordinates), key=order))

        return left + 1 + right


        # n = len(coordinates)
        # dp = [float('inf')] * n
        # for x, y in sorted(coordinates, key=lambda z: (z[0], -z[1])):
        #     if x < coordinates[k][0] and y < coordinates[k][1] or x > coordinates[k][0] and y > coordinates[k][1]:
        #         dp[bisect_left(dp, y)] = y

        # return bisect_left(dp, float('inf')) + 1

        
# @lc code=end

