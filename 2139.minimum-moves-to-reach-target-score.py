#
# @lc app=leetcode id=2139 lang=python3
#
# [2139] Minimum Moves to Reach Target Score
#

# @lc code=start
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        res = 0
        while target > 1 and maxDoubles > 0:
            res += 1 + target % 2
            maxDoubles -= 1
            target >>= 1
        
        return target - 1 + res
        
# @lc code=end

