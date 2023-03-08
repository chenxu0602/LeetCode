#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#

# @lc code=start
import itertools
from typing import List, Generator

class Solution:
    MAX_POWER, MOD = 32, 10**9 + 7

    @classmethod
    def _to_powers(cls, num: int) -> Generator:
        return (p for p in range(cls.MAX_POWER) if num & (1 << p) != 0)

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cum_powers = list(itertools.accumulate(self._to_powers(n), initial=1))
        return [pow(2, cum_powers[r + 1] - cum_powers[l], self.MOD) for l, r in queries]
        
# @lc code=end

