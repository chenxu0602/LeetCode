#
# @lc app=leetcode id=2874 lang=python3
#
# [2874] Maximum Value of an Ordered Triplet II
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        pref_sum = list(accumulate(nums, max))
        suff_sum = list(accumulate(nums[::-1], max))[::-1]


        n, mx = len(nums), 0
        for j in range(1, n - 1):
            mx = max(mx, (pref_sum[j - 1] - nums[j]) * suff_sum[j+1])

        return mx
        
# @lc code=end

