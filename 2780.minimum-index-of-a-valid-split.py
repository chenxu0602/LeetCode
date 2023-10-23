#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        n = len(nums)
        dom, cnt = max(Counter(nums).items(), key=lambda x: x[1])

        left, cut = 0, 2 * cnt - n

        if cut < 2: return -1 

        for i, v in enumerate(nums):
            left += 2 * (v == dom)

            if 1 < left - i <= cut:
                return i


        
# @lc code=end

