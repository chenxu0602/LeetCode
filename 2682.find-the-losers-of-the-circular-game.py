#
# @lc app=leetcode id=2682 lang=python3
#
# [2682] Find the Losers of the Circular Game
#

# @lc code=start
from itertools import accumulate

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        s = set([i for i in range(1, n + 1)])
        for mul in accumulate([i for i in range(n)]):
            if k * mul % n + 1 not in s:
                break
            s.remove(k * mul % n + 1)
        return s
        
# @lc code=end

