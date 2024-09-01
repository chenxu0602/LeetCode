#
# @lc app=leetcode id=3028 lang=python3
#
# [3028] Ant on the Boundary
#

# @lc code=start
from itertools import accumulate

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        return sum(n == 0 for n in accumulate(nums))
        
# @lc code=end

