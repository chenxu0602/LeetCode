#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#
# https://leetcode.com/problems/stone-game-iv/description/
#
# algorithms
# Hard (49.66%)
# Likes:    124
# Dislikes: 13
# Total Accepted:    5.4K
# Total Submissions: 10.9K
# Testcase Example:  '1\r'
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# Initially, there are n stones in a pile.  On each player's turn, that player
# makes a move consisting of removing any non-zero square number of stones in
# the pile.
# 
# Also, if a player cannot make a move, he/she loses the game.
# 
# Given a positive integer n. Return True if and only if Alice wins the game
# otherwise return False, assuming both players play optimally.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: true
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't
# have any moves.
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
# Explanation: Alice can only remove 1 stone, after that Bob removes the last
# one winning the game (2 -> 1 -> 0).
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: true
# Explanation: n is already a perfect square, Alice can win with one move,
# removing 4 stones (4 -> 0).
# 
# 
# Example 4:
# 
# 
# Input: n = 7
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
# If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should
# remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 ->
# 0). 
# If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only
# can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 ->
# 0).
# 
# Example 5:
# 
# 
# Input: n = 17
# Output: false
# Explanation: Alice can't win the game if Bob plays optimally.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 
# 
#

# @lc code=start
from functools import lru_cache
import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # if there is any k that dp[i - k * k] == false, it means we can make the other lose the game
        # Time  complexity: O(N x sqrt(N))
        # Space complexity: O(N)
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(math.sqrt(i) + 1)))
        return dp[-1]


        # DFS with memorization
        # Time  complexity: O(N x sqrt(N))
        # Space complexity: O(N)
        # @lru_cache(None)
        # def dfs(remain):
        #     if remain == 0:
        #         return False

        #     sqrt_root = int(remain ** 0.5)
        #     for i in range(1, sqrt_root + 1):
        #         # if there is any chance to make the opponent lose the game in the next round,
        #         #  then the current player will win.
        #         if not dfs(remain - i * i):
        #             return True

        #     return False

        # return dfs(n)
        
# @lc code=end

