#
# @lc app=leetcode id=2865 lang=python3
#
# [2865] Beautiful Towers I
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        n, ans = len(maxHeights), 0
        for i in range(n):
            ans = max(ans,   sum(accumulate(maxHeights[i::-1], min))
                           + sum(accumulate(maxHeights[i:], min))
                           - maxHeights[i])     # double counted maxHeights[i]

        return ans
        
# @lc code=end

