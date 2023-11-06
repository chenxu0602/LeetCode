#
# @lc app=leetcode id=2862 lang=python3
#
# [2862] Maximum Element-Sum of a Complete Subset of Indices
#

# @lc code=start
from collections import Counter
from math import isqrt

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        # O(sqrt(n))
        n, count = len(nums), Counter()
        for i in range(n):
            x, v = i + 1, 2
            while x >= v * v:
                while x % (v * v) == 0:
                    x //= v * v
                v += 1
            count[x] += nums[i]

        return max(count.values())


        # return max(sum(nums[k * v * v - 1] for v in range(1, isqrt(len(nums) // k) + 1)) for k in range(1, len(nums) + 1))




        
# @lc code=end

