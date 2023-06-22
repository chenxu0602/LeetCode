#
# @lc app=leetcode id=2739 lang=python3
#
# [2739] Total Distance Traveled
#

# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
        
# @lc code=end

