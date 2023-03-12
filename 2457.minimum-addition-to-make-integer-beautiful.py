#
# @lc app=leetcode id=2457 lang=python3
#
# [2457] Minimum Addition to Make Integer Beautiful
#

# @lc code=start
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        n0, i = n, 0
        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            i += 1
        return n * (10 ** i) - n0
        
# @lc code=end

