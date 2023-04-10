#
# @lc app=leetcode id=2587 lang=python3
#
# [2587] Rearrange Array to Maximize Prefix Score
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return sum(n > 0 for n in accumulate(sorted(nums, reverse=True)))
        
# @lc code=end

