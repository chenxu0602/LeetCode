#
# @lc app=leetcode id=2500 lang=python3
#
# [2500] Delete Greatest Value in Each Row
#

# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        return sum(max(c) for c in zip(*[sorted(row) for row in grid]))
        
# @lc code=end

