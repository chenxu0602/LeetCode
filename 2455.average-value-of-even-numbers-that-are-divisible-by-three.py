#
# @lc app=leetcode id=2455 lang=python3
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
import numpy as np

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        return int(np.mean([n for n in nums if n % 6 == 0] or 0))
        
# @lc code=end

