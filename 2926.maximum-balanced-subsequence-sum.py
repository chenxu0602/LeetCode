#
# @lc app=leetcode id=2926 lang=python3
#
# [2926] Maximum Balanced Subsequence Sum
#

# @lc code=start
from bisect import bisect_left, bisect_right, insort

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:

        LIS: list[tuple[int, int]] = [(float("-inf"), 0)]

        for i, v in enumerate(nums):
            if v > 0:
                j = bisect_right(LIS, (v - i, float("inf")))
                if j >= len(LIS): 
                    LIS += (v - i, v + LIS[len(LIS) - 1][1]),
                else:
                    insort(LIS, (v - i, v + LIS[j - 1][1]))

                    while j + 1 < len(LIS) and LIS[j + 1][1] < LIS[j][1]:
                        del LIS[j + 1]

        return LIS[-1][1] if len(LIS) > 1 else max(nums)

        
# @lc code=end

