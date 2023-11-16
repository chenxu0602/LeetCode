#
# @lc app=leetcode id=2909 lang=python3
#
# [2909] Minimum Sum of Mountain Triplets II
#

# @lc code=start
from itertools import accumulate

class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        pref = list(accumulate(nums,       min))
        suff = list(accumulate(nums[::-1], min))[-3::-1]

        return min((p + n + s for p, n, s in zip(pref, nums[1:-1], suff) if p < n > s), default=-1)
        
# @lc code=end

