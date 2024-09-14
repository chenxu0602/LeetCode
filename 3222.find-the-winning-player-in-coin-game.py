#
# @lc app=leetcode id=3222 lang=python3
#
# [3222] Find the Winning Player in Coin Game
#

# @lc code=start
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        y //= 4
        x = min(x, y)

        return 'Alice' if x % 2 == 1 else 'Bob'
        
# @lc code=end

