#
# @lc app=leetcode id=3251 lang=python3
#
# [3251] Find the Count of Monotonic Pairs II
#

# @lc code=start
from math import comb

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(nums)
        max_ = nums.pop(0)

        n1, n2 = 0, max_
        for num in nums:
            if num < n1: return 0

            if num > n1 + n2:
                n1 = num - n2

            n2 = num - n1

            if n2 < max_: max_ = n2

        return comb(n + max_, max_) % MOD        

        
# @lc code=end

