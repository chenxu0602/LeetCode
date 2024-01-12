#
# @lc app=leetcode id=2997 lang=python3
#
# [2997] Minimum Number of Operations to Make Array XOR Equal to K
#

# @lc code=start
from functools import reduce
from operator import xor

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # Count bits of XOR(A) ^ k
        return reduce(xor, nums, k).bit_count()
        
# @lc code=end

