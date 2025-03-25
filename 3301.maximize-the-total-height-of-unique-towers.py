#
# @lc app=leetcode id=3301 lang=python3
#
# [3301] Maximize the Total Height of Unique Towers
#

# @lc code=start
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:

        maximumHeight.sort(reverse=True)
        sm = height = maximumHeight[0]

        for tower in maximumHeight[1:]:
            height = min(height - 1, tower)
            if height == 0: return -1
            sm += height

        return sm


        
# @lc code=end

