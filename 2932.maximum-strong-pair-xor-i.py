#
# @lc app=leetcode id=2932 lang=python3
#
# [2932] Maximum Strong Pair XOR I
#

# @lc code=start
from itertools import product

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        return max((x ^ y for x, y in product(nums, repeat=2) if abs(x - y) <= min(x, y)), default=0)
        
# @lc code=end

