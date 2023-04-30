#
# @lc app=leetcode id=2660 lang=python3
#
# [2660] Determine the Winner of a Bowling Game
#

# @lc code=start
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def fn(player):
            ans = 0
            for i, x in enumerate(player):
                ans += x
                if i and player[i - 1] == 10 or i >= 2 and player[i - 2] == 10:
                    ans += x
            return ans

        diff = fn(player1) - fn(player2)
        return 1 if diff > 0 else 2 if diff < 0 else 0
        
# @lc code=end

