#
# @lc app=leetcode id=3012 lang=python3
#
# [3012] Minimize Length of Array Using Operations
#

# @lc code=start
from functools import reduce
from math import gcd

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:

        # v = min(nums)
        # for x in nums:
        #     if x % v:
        #         return 1
        # return (nums.count(v) + 1) // 2

        return max(1, nums.count(reduce(gcd, nums))) + 1 >> 1
        
# @lc code=end

