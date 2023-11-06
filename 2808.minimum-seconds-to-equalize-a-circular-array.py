#
# @lc app=leetcode id=2808 lang=python3
#
# [2808] Minimum Seconds to Equalize a Circular Array
#

# @lc code=start
from collections import defaultdict
from itertools import pairwise

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:

        nums += nums
        indices = defaultdict(list)
        for i, v in enumerate(nums):
            indices[v] += i,
        return min(max(b - a for a, b in pairwise(l)) // 2 for l in indices.values())
        
# @lc code=end

