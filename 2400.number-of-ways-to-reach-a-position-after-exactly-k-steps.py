#
# @lc app=leetcode id=2400 lang=python3
#
# [2400] Number of Ways to Reach a Position After Exactly k Steps
#

# @lc code=start
from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (startPos - endPos - k) % 2:
            return 0

        return comb(k, (endPos - startPos + k) // 2) % (10**9 + 7)
        
# @lc code=end

