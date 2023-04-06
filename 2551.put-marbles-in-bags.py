#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
import heapq
from itertools import pairwise

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        w = [a + b for a, b in pairwise(weights)]
        return sum(heapq.nlargest(k - 1, w)) - sum(heapq.nsmallest(k - 1, w))
        
# @lc code=end

