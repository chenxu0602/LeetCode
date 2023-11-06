#
# @lc app=leetcode id=2817 lang=python3
#
# [2817] Minimum Absolute Difference Between Elements With Constraint
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        if x == 0: return 0
        res = float("inf")
        S = SortedList()
        n = len(nums)

        for i in range(n):
            j = S.bisect_left(nums[i])
            if j < len(S):
                res = min(res, abs(S[j] - nums[i]))
            if j > 0:
                res = min(res, abs(S[j - 1] - nums[i]))
            if i >= x - 1:
                S.add(nums[i - (x - 1)])

        return res

        
# @lc code=end

