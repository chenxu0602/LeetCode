#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
from itertools import accumulate

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last = {c: i for i, pgm in enumerate(garbage) for c in pgm}
        dis = list(accumulate(travel, initial=0))
        return sum(map(len, garbage)) + sum(dis[last.get(c, 0)] for c in "PGM")
        
# @lc code=end

