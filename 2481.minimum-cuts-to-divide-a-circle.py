#
# @lc app=leetcode id=2481 lang=python3
#
# [2481] Minimum Cuts to Divide a Circle
#

# @lc code=start
class Solution:
    def numberOfCuts(self, n: int) -> int:

        if n == 1: return 0
        return n if n % 2 else n // 2
        
# @lc code=end

