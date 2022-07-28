#
# @lc app=leetcode id=2344 lang=python3
#
# [2344] Minimum Deletions to Make Array Divisible
#

# @lc code=start
from functools import reduce 
from math import gcd

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # div = reduce(gcd, numsDivide)
        # return next((i for i, v in enumerate(sorted(nums)) if div % v == 0), -1)

        div = reduce(gcd, numsDivide)
        min_ = min(filter(lambda x: div % x == 0, nums), default=-1)
        return -1 if min_ == -1 else sum(x < min_ for x in nums)
        
# @lc code=end

