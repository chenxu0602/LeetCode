#
# @lc app=leetcode id=2790 lang=python3
#
# [2790] Maximum Number of Groups With Increasing Length
#

# @lc code=start
from collections import Counter

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:

        usageLimits.sort()
        total = k = 0
        for lim in usageLimits:
            total += lim
            if total >= (k + 1) * (k + 2) // 2:
                k += 1
        return k

        
# @lc code=end

