#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        count = Counter(ranks)
        left, right = 1, min(count) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if sum(math.isqrt(mid // c) * count[c] for c in count) < cars:
                left = mid + 1
            else:
                right = mid
        return left

        
# @lc code=end

