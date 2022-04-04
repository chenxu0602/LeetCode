#
# @lc app=leetcode id=2136 lang=python3
#
# [2136] Earliest Possible Day of Full Bloom
#

# @lc code=start
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        """
        res = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            res = max(res, grow) + plant
        return res
        """

        tot = cur = 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            tot = max(tot, cur + grow + plant)
            cur += plant

        return tot
        
# @lc code=end

