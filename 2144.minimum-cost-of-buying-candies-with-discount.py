#
# @lc app=leetcode id=2144 lang=python3
#
# [2144] Minimum Cost of Buying Candies With Discount
#

# @lc code=start
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(cost) - sum(sorted(cost)[-3::-3])
        
# @lc code=end

