#
# @lc app=leetcode id=2240 lang=python3
#
# [2240] Number of Ways to Buy Pens and Pencils
#

# @lc code=start
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        ways = 0
        for i in range(1 + total // cost1):
            left = max(total -i * cost1, 0)
            ways += 1 + left // cost2
        return ways
        
# @lc code=end

