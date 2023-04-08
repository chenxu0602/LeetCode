#
# @lc app=leetcode id=2561 lang=python3
#
# [2561] Rearranging Fruits
#

# @lc code=start
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        count = Counter(basket1 + basket2)
        for c in count:
            if count[c] % 2:
                return -1
            count[c] >>= 1

        a2 = list((Counter(basket1) - count).elements())
        b2 = list((Counter(basket2) - count).elements())

        small = min(count)
        c = sorted(a2 + b2)
        return sum(min(small * 2, c[i]) for i in range(len(a2)))

        
# @lc code=end

