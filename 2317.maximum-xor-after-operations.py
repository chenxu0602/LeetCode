#
# @lc app=leetcode id=2317 lang=python3
#
# [2317] Maximum XOR After Operations 
#

# @lc code=start
from functools import reduce

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(ior, nums)
        
# @lc code=end

