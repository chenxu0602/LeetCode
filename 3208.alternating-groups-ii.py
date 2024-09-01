#
# @lc app=leetcode id=3208 lang=python3
#
# [3208] Alternating Groups II
#

# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        n = len(colors)
        colors += colors[:k - 1]
        res, cnt = 0, 1

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res += 1

        return res
    
        
# @lc code=end

