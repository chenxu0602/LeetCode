#
# @lc app=leetcode id=2750 lang=python3
#
# [2750] Ways to Split Array Into Good Subarrays
#

# @lc code=start
from operator import mul
from functools import reduce

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        if 1 not in nums: return 0
        nums = ''.join(map(str, nums)).strip('0').split('1')
        return reduce(mul, list(map(lambda x: 1 + len(x), nums))) % MOD
        
# @lc code=end

