#
# @lc app=leetcode id=2849 lang=python3
#
# [2849] Determine if a Cell Is Reachable at a Given Time
#

# @lc code=start
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        width  = abs(sx - fx)
        height = abs(sy - fy)
        if width == 0 and height == 0 and t == 1:
            return False 

        return t >= max(width, height)
        
# @lc code=end

