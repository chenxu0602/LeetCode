#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#
# https://leetcode.com/problems/design-tic-tac-toe/description/
#
# algorithms
# Medium (49.83%)
# Likes:    382
# Dislikes: 31
# Total Accepted:    48.2K
# Total Submissions: 96.4K
# Testcase Example:  '["TicTacToe","move","move","move","move","move","move","move"]\n' +
#
# Design a Tic-tac-toe game that is played between two players on a n x n
# grid.
# 
# 
# You may assume the following rules:
# 
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical,
# or diagonal row wins the game.
# 
# 
# 
# Example:
# 
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
# 
# TicTacToe toe = new TicTacToe(3);
# 
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
# 
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
# 
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
# 
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
# 
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
# 
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
# 
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# 
# 
# 
# Follow up:
# Could you do better than O(n^2) per move() operation?
# 
#
from collections import Counter

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """

        self.size = n
        self.count = Counter()
        

    def move(self, row: int, col: int, player: int) -> int:

        for i, x in enumerate((row, col, row+col, row-col)):
            self.count[i, x, player] += 1
            if self.count[i, x, player] == self.size:
                return player
            return 0

    
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

