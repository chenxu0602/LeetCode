#
# @lc app=leetcode id=2543 lang=python3
#
# [2543] Check if Point Is Reachable
#

# @lc code=start
import math 

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:

        v = math.gcd(targetX, targetY)
        return v == (v & -v)
        
# @lc code=end

