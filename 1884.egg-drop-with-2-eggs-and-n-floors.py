#
# @lc app=leetcode id=1884 lang=python3
#
# [1884] Egg Drop With 2 Eggs and N Floors
#

# @lc code=start
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def twoEggDrop(self, n: int) -> int:
        return min((1 + max(i - 1, self.twoEggDrop(n - i)) for i in range(1, n)), default=1)


        
# @lc code=end

