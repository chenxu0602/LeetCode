#
# @lc app=leetcode id=2501 lang=python3
#
# [2501] Longest Square Streak in an Array
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        sqr = Counter(set(nums))
        for n in sqr:
            while (s := math.isqrt(n)) ** 2 == n and s in sqr:
                sqr[s] += 1
                n = s

        return c if (c := max(sqr.values())) >= 2 else -1
        
# @lc code=end

