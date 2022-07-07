#
# @lc app=leetcode id=2320 lang=python3
#
# [2320] Count Number of Ways to Place Houses
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        a, b, MOD = 1, 1, 10**9 + 7
        for i in range(n):
            a, b = b, (a + b) % MOD
        return b * b % MOD
        
# @lc code=end

