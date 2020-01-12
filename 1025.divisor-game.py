#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#
# https://leetcode.com/problems/divisor-game/description/
#
# algorithms
# Easy (64.19%)
# Likes:    157
# Dislikes: 462
# Total Accepted:    25.1K
# Total Submissions: 38.4K
# Testcase Example:  '2'
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# Initially, there is a number N on the chalkboard.  On each player's turn,
# that player makes a move consisting of:
# 
# 
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# 
# 
# Also, if a player cannot make a move, they lose the game.
# 
# Return True if and only if Alice wins the game, assuming both players play
# optimally.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
# moves.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
#
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
        

