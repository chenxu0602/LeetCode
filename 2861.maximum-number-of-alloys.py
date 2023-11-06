#
# @lc app=leetcode id=2861 lang=python3
#
# [2861] Maximum Number of Alloys
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        def calc_need(x):
            for comp in composition:
                need = sum(max(0, cp * x - st) * co for cp, st, co in zip(comp, stock, cost))
                if need <= budget: return False
            return True

        rng = range(min(stock) + budget + 1)

        return bisect_left(rng, True, key=calc_need) - 1
        
# @lc code=end

