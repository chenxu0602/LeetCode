#
# @lc app=leetcode id=2550 lang=python3
#
# [2550] Count Collisions of Monkeys on a Polygon
#

# @lc code=start
class Solution:
    def monkeyMove(self, n: int) -> int:

        MOD = 10**9 + 7
        return (pow(2, n, MOD) - 2) % MOD
        
# @lc code=end

