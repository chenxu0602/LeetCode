#
# @lc app=leetcode id=2335 lang=python3
#
# [2335] Minimum Amount of Time to Fill Cups
#

# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:

        return max(max(amount), (sum(amount) + 1) // 2)
        
# @lc code=end

