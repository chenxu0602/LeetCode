#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
from itertools import groupby, chain

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        grp = groupby(nums, key=lambda x: x.bit_count())
        return list(chain(*[sorted(g) for _, g in grp])) == sorted(nums)
        
# @lc code=end

