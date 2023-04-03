#
# @lc app=leetcode id=2527 lang=python3
#
# [2527] Find Xor-Beauty of Array
#

# @lc code=start
from functools import reduce 

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)
        
# @lc code=end

